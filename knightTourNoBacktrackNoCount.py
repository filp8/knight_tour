from time import time
from typing import Callable

from boardUtil import creaGrafo
from boardToString import save_board

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion


def percorsoCavalloNoBackNoCount(n:int, timeOut:float, criterioScelta:Callable[[int, int, list[int]], float], nomeFile:str=None, stepSave:int=1, asTab:bool=False, simboli:tuple[str]=('⬜','⬛️','🟥'), id:int=0):
    if n<3:
        return (n,0,None)
    
    start = time()
    graph = creaGrafo(n)
    nelPath = [0]*(n*n)
    path = []
    
    pos = 0
    path.append(pos)
    nelPath[pos]=1
    
    cnt_it = 0
    while True:
        #print(f'n={n} iterazioni={cnt_it} backtrack={0}')
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
        
        # initialize neighbours and sort by criterioScelta 
        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
        neighbor_list.sort(key = lambda neig: criterioScelta(n,neig,1))
        
        if neighbor_list==[]:
            return (n,time()-start,[]) # No solution without backtraching
        else:
            pos=neighbor_list[0] # move to first remaining neighbor
            path.append(pos)
            nelPath[pos]=1


if __name__ == '__main__':
    n=7
    criterioScelta=eurMenoEntrantiDistCentroEuclidea
    timeOut=3600*24*7
    nomeFile=None
    
    result=percorsoCavalloNoBackNoCount(n, timeOut, criterioScelta, nomeFile)
    print(result)



