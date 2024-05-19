from time import time
import os
from pathlib import Path

import csv

from boardUtil import isValidSolution

from knightTour import percorsoCavalloIterativo
from knightTourNoBacktrack import percorsoCavalloNoBack
from knightTourNoBacktrackNoCount import percorsoCavalloNoBackNoCount
from knightTourRicorsivo import percorsoCavalloRicorsivo

from criteriSceltaHamilton import eurDistCentroEuclidea,eurMenoEntrantiDistCentroEuclidea,eurMenoEntranti,\
eurDistCentroManhattan,eurMenoEntrantiDistCentroManhattan



def file_exists(filename):
        return os.path.isfile(filename)

def record_exists(filename, numero,nomeAlgoritmo,nomeEuristica):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta l'intestazione
        for row in reader:
            num,nomA,nomE,tim,esi=row
            if int(num) == numero and nomA == nomeAlgoritmo and nomE==nomeEuristica:
                return True
    return False

def find_max(filename:str, max_index:int, algorithmName:str, algo_index:int, euristicName:str, eur_index:int):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta l'intestazione
        max = 0
        for row in reader:
            if algorithmName==row[algo_index] and euristicName==row[eur_index]:
                # record con uguale algo ed eur
                conf=int(row[max_index])
                if conf>max:
                    max = conf
    return max

def cercaNumeriCriticiVariAlgoritmi(inizio,fine,step,timeOut,algoritmi,euristiche,outDataFileName):
    for algoritmo in algoritmi:
        for euristica in euristiche:
            if not (algoritmo.__name__=='percorsoCavalloNoBackNoCount' and euristica.__name__[:15] == 'eurMenoEntranti'):
                cercaNumeriCritici(inizio,fine,step,timeOut,algoritmo,euristica,outDataFileName)
    return

def cercaNumeriCritici(inizio,fine,step,timeOut,algoritmo,criterioScelta,outDataFileName, writeThreshold=10):
    minDelta=100
    
    fail = []
    gooal = []
    nonRisolvibili = []
    record = []

    algoritmName = algoritmo.__name__
    euristicName = criterioScelta.__name__
    
    if inizio<1:
        inizio = 1

    if file_exists(outDataFileName):
        numero,tempo,esito = algoritmo(inizio,time(),timeOut,criterioScelta)
        if record_exists(outDataFileName,numero,algoritmName,euristicName):
            inizio = find_max(outDataFileName, 0, algoritmName, 1,euristicName, 2)+1
            if fine<=inizio:
                fine = inizio + minDelta
    else:
        outDataFolderName=os.path.dirname(outDataFileName)
        Path(outDataFolderName).mkdir(parents=True, exist_ok=True)
        with open(outDataFileName, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([['numero','nome algoritmo','nome euristica','tempo secondi','risultato']])
        

    for n in range(inizio,fine,step):
        numero,tempo,esito = algoritmo(n,time(),timeOut,criterioScelta)
        ris = esito if esito == None else False if esito == [] else True 
        temp = format(tempo,'.4f')

        record.append([numero,algoritmName,euristicName,temp,ris])

        if esito==None:
            nonRisolvibili.append(numero)
            print(f'n={n} UNSOLVABLE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        elif esito ==[]:
            fail.append(numero)
            print(f'n={n} FAILED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        else:
            gooal.append(numero)
            print(f'n={n} found in {tempo:.3f}sec')
            if not isValidSolution(n, esito):
                print(f'n={n} INVALID SOLUTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        if not n % writeThreshold:
            with open(outDataFileName, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(record)
            record.clear()

    with open(outDataFileName, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(record)

    return fail,gooal,nonRisolvibili


if __name__ == '__main__':

    inizio = 0
    fine = 20
    step = 1
    timeOut = 1.0
    outDataFileName = './data/data3.csv'
    algoritmi = [percorsoCavalloIterativo,percorsoCavalloNoBack,percorsoCavalloNoBackNoCount,percorsoCavalloRicorsivo]
    euristiche = [eurDistCentroEuclidea,eurMenoEntrantiDistCentroEuclidea,eurMenoEntranti,eurDistCentroManhattan,eurMenoEntrantiDistCentroManhattan]

    cercaNumeriCriticiVariAlgoritmi(inizio,fine,step,timeOut,algoritmi,euristiche,outDataFileName)




    #   NUMERI CRITICI SINGOLO ALGORITMO
    # inizio = 0
    # fine = 10000
    # step = 1
    # timeOut = 100.0
    # outDataFileName = './data/data1.csv'
    # fail,gooal,nonRisolvibili = cercaNumeriCritici(inizio,fine,step,timeOut,percorsoCavalloNoBack,eurMenoEntrantiDistCentroManhattan,outDataFileName)

    # print(gooal)
    # print()
    # print(fail)
    # print(f'\n\n inizio:{inizio}     fine:{fine}     step:{step}     timeOut:{timeOut}')
    # print(f'\n goal:{len(gooal)}')
    # print(f'\n fail:{len(fail)}')
    # print(f'\n nonRisolvibili:{len(nonRisolvibili)}')

    # print(find_max('./data/data1.csv',0))
