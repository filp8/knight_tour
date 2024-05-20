from time import time
from typing import Callable

from boardUtil import idxToCord,creaGrafo,make_cnt,update_cnt
from boardToString import save_board

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion


def percorsoCavalloNoBack(n:int, timeOut:float, criterioScelta:Callable[[int, int, list[int]], float], nomeFile:str=None, stepSave:int=1, asTab:bool=False, simboli:tuple[str]=('⬜','⬛️','🟥'), id:int=0):
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

        x,y = idxToCord(n,pos)
        update_cnt(n,x,y,move_cnt,nelPath,dec=True)
        
        # initialize neighbours and sort by criterioScelta 
        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
        neighbor_list.sort(key = lambda neig: criterioScelta(n,neig,move_cnt[neig]))
        
        if neighbor_list==[]:
            return (n,time()-start,[]) # No solution without backtraching
        else:
            pos=neighbor_list[0] # move to first remaining neighbor
            path.append(pos)
            nelPath[pos]=1
            stackNL.append(neighbor_list[1:]) # push trailing neighbours


if __name__ == '__main__':
    n=7
    criterioScelta=eurMenoEntrantiDistCentroEuclidea
    timeOut=3600*24*7
    nomeFile=None
    
    result=percorsoCavalloNoBack(n, timeOut, criterioScelta, nomeFile)
    print(result)
