from time import time
import os
from pathlib import Path

import csv

from boardUtil import isValidSolution

from knightTour import percorsoCavalloIterativo
from provaStack import percorsoCavalloStack
from knightTourNoBacktrack import percorsoCavalloNoBack
from knightTourNoBacktrackNoCount import percorsoCavalloNoBackNoCount
from knightTourNoGraph import percorsoCavalloIterativoNoGraph
from knightTourRicorsivo import percorsoCavalloRicorsivo

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion



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

def find_max(filename:str, max_index:int, algorithmName:str, algo_index:int, euristicName:str, eur_index:int, timeOut:str, timeOut_index:int, result_index:int):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta l'intestazione
        max = 0
        for row in reader:
            if row[result_index]=='True' and row[algo_index]==algorithmName and row[eur_index]==euristicName and row[timeOut_index]>=timeOut:
                # record con uguale algo ed eur
                conf=int(row[max_index])
                if conf>max:
                    max = conf
    return max

def find_not_done_n_list(filename:str, min_n:int, max_n:int, step:int, algorithmName:str, euristicName:str, timeOut:float)->list[int]:
    n_index:int=0
    algo_index:int=1
    eur_index:int=2
    timeOut_index:int=3
    result_index:int=5
    
    isToDoArr=[True]*(max_n-min_n+1)
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta l'intestazione
        for row in reader:
            rec_n=int(row[n_index])
            rec_algo=row[algo_index]
            rec_eur=row[eur_index]
            rec_timeout=float(row[timeOut_index])
            rec_result_str=row[result_index]
            rec_completed = rec_result_str!='False'
            
            isDone =    (min_n <= rec_n <= max_n) and \
                        ((rec_n-min_n)%step==0)   and \
                        rec_algo==algorithmName   and \
                        rec_eur==euristicName     and \
                        (rec_completed or (not rec_completed and rec_timeout >= timeOut))
                            
            if isDone:
                isToDoArr[rec_n-min_n] = False
    return [n+min_n for n, isToDo in enumerate(isToDoArr) if isToDo]

def cercaNumeriCriticiVariAlgoritmi(inizio,fine,step,timeOut,algoritmi,euristiche,outDataFileName):
    for algoritmo in algoritmi:
        for euristica in euristiche:
            if not (algoritmo.__name__=='percorsoCavalloNoBackNoCount' and euristica.__name__[:15] == 'eurMenoEntranti'):
                algoEurNames=f'algoritmo={algoritmo.__name__} euristica={euristica.__name__}:'
                print("\n"+algoEurNames)
                fail,goal,nonRisolvibili=cercaNumeriCritici(inizio,fine,step,timeOut,algoritmo,euristica,outDataFileName)
                print(algoEurNames)
                print(f'   fail={str(len(fail)) if fail else "None"}; goal={str(len(goal)) if goal else "None"}; unsolvable={str(len(nonRisolvibili)) if nonRisolvibili else "None"};')

    return

def cercaNumeriCritici(inizio,fine,step,timeOut,algoritmo,criterioScelta,outDataFileName, writeThreshold=10):
    
    fail = []
    goal = []
    nonRisolvibili = []
    record = []

    algorithmName = algoritmo.__name__
    euristicName = criterioScelta.__name__
    
    if inizio<1:
        inizio = 1
        
    if file_exists(outDataFileName):
        nToDoList=find_not_done_n_list(outDataFileName, inizio, fine, step, algorithmName, euristicName, timeOut)
    else:
        Path(os.path.dirname(outDataFileName)).mkdir(parents=True, exist_ok=True) # make dir if not exists
        with open(outDataFileName, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([['numero','nome algoritmo','nome euristica','time_out','tempo secondi','risultato']])
        nToDoList=[n for n in range(inizio, fine+1, step)]
    
    if not nToDoList:
        print(f'Fatti tutti in [{inizio}, {fine}] con timeout>={timeOut}.')
        return (None, None, None)

    print(f'nToDoList={nToDoList}')
    for n in nToDoList:
        numero,tempo,esito = algoritmo(n,time(),timeOut,criterioScelta)
        ris = str(len(esito)>0 if esito!=None else 'UNSOLVABLE')

        if esito==None:
            nonRisolvibili.append(numero)
            print(f'n={n} UNSOLVABLE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        elif esito ==[]:
            fail.append(numero)
            print(f'n={n} FAILED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        else:
            goal.append(numero)
            print(f'n={n} found in {tempo:.3f}sec')
            if not isValidSolution(n, esito):
                print(f'n={n} INVALID SOLUTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                ris='ERROR'
                
        record.append([numero,algorithmName,euristicName,timeOut,format(tempo,'.4f'),ris])

        if not n % writeThreshold:
            with open(outDataFileName, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(record)
            record.clear()

    with open(outDataFileName, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(record)

    return fail,goal,nonRisolvibili


if __name__ == '__main__':
    # start=time()
    
    # inizio = 1700
    # fine = 1700
    # step = 1
    # timeOut = 600.0
    # outDataFileName = './data/data4.csv'
    
    # # algoritmi = [percorsoCavalloIterativo,percorsoCavalloNoBack,percorsoCavalloNoBackNoCount,percorsoCavalloRicorsivo,percorsoCavalloStack]
    # # euristiche = [eurDistCentroEuclidea,eurMenoEntrantiDistCentroEuclidea,eurMenoEntranti,eurDistCentroManhattan,eurMenoEntrantiDistCentroManhattan]
    # algoritmi = [percorsoCavalloIterativo, percorsoCavalloNoBack]
    # # algoritmi = [percorsoCavalloIterativoNoGraph]
    # euristiche = [eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan]

    # cercaNumeriCriticiVariAlgoritmi(inizio,fine,step,timeOut,algoritmi,euristiche,outDataFileName)
    
    # print(time()-start)

    #   NUMERI CRITICI SINGOLO ALGORITMO
    inizio = 0
    fine = 10000
    step = 1
    timeOut = 1.0
    outDataFileName = './data/data2.csv'
    fail,goal,nonRisolvibili = cercaNumeriCritici(inizio, fine, step, timeOut, percorsoCavalloStack,eurMenoEntrantiDistCentroEuclidea, outDataFileName)

    print(goal)
    print()
    print(fail)
    print(f'\n\n inizio:{inizio}     fine:{fine}     step:{step}     timeOut:{timeOut}')
    print(f'\n goal:{str(len(goal)) if goal else "None"}')
    print(f'\n fail:{str(len(fail)) if fail else "None"}')
    print(f'\n nonRisolvibili:{str(len(nonRisolvibili)) if nonRisolvibili else "None"}')

    print(find_max('./data/data1.csv',0))
