from time import time
from typing import Callable
from boardUtil import idxToCord,creaGrafo,make_cnt,update_cnt,isValidSolution,cordToIdx
from boardToString import save_board,print_board

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion

def addOnStack(stack,pos,adiList):
    stack.append((pos,adiList))
    return

def unpackStack(stack):
    pathOut = []
    for el in stack:
        pathOut.append(el[0])
    return pathOut


def percorsoCavalloStack(n:int, start:float, timeOut:float, criterioScelta:Callable[[int, int, list[int]], float], nomeFile:str=None, stepSave:int=1, asTab:bool=False, simboli:tuple[str]=('⬜','⬛️','🟥'), id:int=0):
    if n<3:
        return (n,0,None)
    
    start = time()
    graph = creaGrafo(n)
    nelPath = [0]*(n*n)
    move_cnt = make_cnt(n)

    stack = []
    pos = 0
    secondaMossa = cordToIdx(n,1,2)
    addOnStack(stack,pos,[secondaMossa])
    nelPath[pos]=1
    update_cnt(n,0,0,move_cnt,nelPath,dec=True)
    pos = secondaMossa
    nelPath[pos]=1
    isBackTrack = False
    while True:
        #print_board(nelPath,n)
        toDoCount=len(graph)-len(stack)
        if toDoCount==0:
            return (n,time()-start,unpackStack(stack))
        isLast = (toDoCount == 1)

        if not isBackTrack:
            x,y = idxToCord(n,pos)
            backtrackPredicted = update_cnt(n,x,y,move_cnt,nelPath,dec=True)
            isBackTrack = not isLast and False
        
        if isBackTrack:
            isBackTrack = False
            
            if stack == []: 
                return (n,time()-start,None)   
            
            update_cnt(n,x,y,move_cnt,nelPath,dec=False)
            nelPath[pos]=0
            pos,neighbor_list = stack.pop()
        else:
            neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
            neighbor_list.sort(key = lambda neig: criterioScelta(n,neig,move_cnt))
        
        if neighbor_list==[]:
            if not isLast:
                isBackTrack = True 
            else:
                addOnStack(stack,pos,[])
        else:
            nelPath[pos]=1
            addOnStack(stack,pos,neighbor_list[1:])
            pos=neighbor_list[0]
            
    


if __name__ == '__main__':
    n=5
    start=None
    criterioScelta=eurMenoEntrantiDistCentroEuclidea
    timeOut=3600*24*7
    nomeFile='./txt/provaiterativa2.txt'
    #nomeFile=None

    numero,tempo,esito =percorsoCavalloIterativo(n, start, timeOut, criterioScelta, nomeFile)
    print(numero,tempo,esito)
    if esito and not isValidSolution(n, esito):
        print(f'n={n} INVALID SOLUTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
