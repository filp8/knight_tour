from time import time
from typing import Callable
from boardUtil import idxToCord,creaGrafo,make_cnt,update_cnt,isValidSolution
from boardToString import save_board

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion


def percorsoCavalloIterativo(n:int, start:float, timeOut:float, criterioScelta:Callable[[int, int, list[int]], float], nomeFile:str=None, stepSave:int=1, asTab:bool=False, simboli:tuple[str]=('⬜','⬛️','🟥'), id:int=0):
    if n<3:
        return (n,0,None)
    
    start = time()
    graph = creaGrafo(n)
    nelPath = [0]*(n*n)
    move_cnt = make_cnt(n)
    path = []
    stackNL = []
    
    pos = 0
    path.append(pos)
    nelPath[pos]=1
    isBackTrack = False
    cnt_it = 0
    cnt_back = 0
    while True:
        #print(f'n={n} iterazioni={cnt_it} backtrack={cnt_back}')
        if timeOut and time()-start>timeOut:
            return (n,time()-start,[])
        cnt_it+=1

        if nomeFile and id%stepSave==0: 
            save_board(nelPath,n,pos,nomeFile,id,asTab,simboli)
            print(f'saveId={id}')
        id+=1

        toDoCount=len(graph)-len(path)
        if not toDoCount:
            return (n,time()-start,path)
        isLast = (toDoCount == 1)

        if not isBackTrack:
            x,y = idxToCord(n,pos)
            backtrackPredicted = update_cnt(n,x,y,move_cnt,nelPath,dec=True)
            isBackTrack = not isLast and backtrackPredicted
        
        if isBackTrack:
            isBackTrack = False
            cnt_back+=1
            
            if not path or path == [0]: # backtrached to the origin, only symmetrical status is left
                return (n,time()-start,None)    # No solution for this size
            
            # do backtraching updates
            nelPath[pos]=0
            update_cnt(n,x,y,move_cnt,nelPath,dec=False)
            # pop pos
            path.pop()
            pos = path[-1]
            # pop neighbor_list
            neighbor_list = stackNL.pop()
        else:
            # initialize neighbours and sort by criterioScelta 
            neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
            neighbor_list.sort(key = lambda neig: criterioScelta(n,neig,move_cnt))
        
        if neighbor_list==[]:
            isBackTrack = True # all neigbour where excluded
        else:
            pos=neighbor_list[0] # move to first remaining neighbor
            path.append(pos)
            nelPath[pos]=1
            stackNL.append(neighbor_list[1:]) # push trailing neighbours


if __name__ == '__main__':
    n=7
    start=None
    criterioScelta=eurMenoEntrantiDistCentroEuclidea
    timeOut=3600*24*7
    nomeFile='./txt/provaiterativa2.txt'
    #nomeFile=None

    numero,tempo,esito =percorsoCavalloIterativo(n, start, timeOut, criterioScelta, nomeFile)
    print(numero,tempo,esito)
    if esito and not isValidSolution(n, esito):
        print(f'n={n} INVALID SOLUTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
