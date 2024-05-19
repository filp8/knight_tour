from time import time
import os  
import csv
import operator

from boardUtil import isValidSolution

from knightTour import percorsoCavalloIterativo
from knightTourNoBacktrack import percorsoCavalloNoBack
from knightTourRicorsivo import percorsoCavalloRicorsivo

from criteriSceltaHamilton import eurDistCentroEuclidea,eurMenoEntrantiDistCentroEuclidea,eurMenoEntranti,\
eurDistManhattan,eurMenoEntrantiDistCentroManhattan



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

def find_max(filename, column_index):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta l'intestazione
        max = 0
        for row in reader:
            conf=int(row[column_index])
            if conf>max:
                max = conf
    return max

def cercaNumeriCritici(inizio,fine,step,timeOut,algoritmo,criterioScelta,outDataFileName):
    fail = []
    gooal = []
    nonRisolvibili = []
    record = []

    algoritmName = str(algoritmo).split(' ')[1]
    euristicName = str(criterioScelta).split(' ')[1]
    
    if inizio<5:
        inizio = 5

    if file_exists(outDataFileName):
        numero,tempo,esito = algoritmo(inizio,time(),timeOut,criterioScelta)
        if record_exists(outDataFileName,numero,algoritmName,euristicName):
            inizio = find_max(outDataFileName,0)+1
            if fine<=inizio:
                fine = inizio+100

    for n in range(inizio,fine,step):
        numero,tempo,esito = algoritmo(n,time(),timeOut,criterioScelta)
        ris = esito if esito == None else False if esito == [] else True 
        temp = format(tempo,'.4f')

        record.append([numero,algoritmName,euristicName,temp,ris])
        print((numero,tempo))

        if esito==None:
            nonRisolvibili.append(numero)
        elif esito ==[]:
            fail.append(numero)
            print(f'n={n} FAILED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        else:
            gooal.append(numero)
            print(f'n={n} found in {ret[1]:.3f}sec')
            if not isValidSolution(n, esito):
                print(f'n={n} INVALID SOLUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            
    
    if file_exists(outDataFileName):
        with open(outDataFileName, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(record)
    else:
        with open(outDataFileName, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([['numero','nome algoritmo','nome euristica','tempo secondi','risultato']])
            writer.writerows(record)


    return fail,gooal,nonRisolvibili


if __name__ == '__main__':
    inizio = 0
    fine = 1000
    step = 1
    timeOut = 1000.0
    outDataFileName = './data/data1.csv'

    fail,gooal,nonRisolvibili = cercaNumeriCritici(inizio,fine,step,timeOut,percorsoCavalloNoBack,eurDistManhattan,outDataFileName)

    print(gooal)
    print()
    print(fail)
    print(f'\n\n inizio:{inizio}     fine:{fine}     step:{step}     timeOut:{timeOut}')
    print(f'\n goal:{len(gooal)}')
    print(f'\n fail:{len(fail)}')
    print(f'\n nonRisolvibili:{len(nonRisolvibili)}')

    # print(find_max('./data/data1.csv',0))
