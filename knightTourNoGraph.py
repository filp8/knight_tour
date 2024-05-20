from time import time
from typing import Callable
from boardUtil import idxToCord, cordToIdx, creaGrafo,make_cnt,update_cnt,isValidSolution, getMosseCavallo
from boardToString import save_board

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion

def getUnvisitedNeighbours(n:int, fromPos:int, isInPath:list[int])->list[int]:
    outList:list[int]=[]
    mosse_cavallo:list[tuple[int,int]] = getMosseCavallo()
    fromX, fromY = idxToCord(n,fromPos)
    for dX,dY in mosse_cavallo:
        toX = fromX+dX
        toY = fromY+dY
        toPos=cordToIdx(n, toX, toY)
        if 0<=toX<n and 0<=toY<n and not isInPath[toPos]:
            outList.append(toPos)
    return outList
        
def getUnvisitedNeighboursWithCount(n:int, fromPos:int, isInPath:list[int])->list[tuple[int,int]]:
    outList:list[tuple[int,int]]=[]
    unvisitedNeighbours = getUnvisitedNeighbours(n, fromPos, isInPath)
    for neighPos in unvisitedNeighbours:
        nnl=getUnvisitedNeighbours(n, neighPos, isInPath)
        outList.append((neighPos, len(nnl)))
    return outList
    
    
def percorsoCavalloIterativoNoGraph(n:int, timeOut:float, criterioScelta:Callable[[int, int, list[int]], float], nomeFile:str=None, stepSave:int=1, asTab:bool=False, simboli:tuple[str]=('⬜','⬛️','🟥'), id:int=0):
    start = time()
    if n<3:
        return (n,0,None)
    
    cellCount=n*n
    isInPath = [0]*(cellCount)
    path = []
    
    pos = 0
    path.append(pos)
    isInPath[pos]=1
    
    isBackTrack = False

    while True:
        if timeOut and time()-start>timeOut:
            return (n,time()-start,[])

        if nomeFile and id%stepSave==0: 
            save_board(isInPath,n,pos,nomeFile,id,asTab,simboli)
            print(f'saveId={id}')
        id+=1

        toDoCount=cellCount-len(path)
        if not toDoCount:
            return (n,time()-start,path)
        isLast = (toDoCount == 1)

        if isBackTrack:
            isBackTrack = False
            
            if not path or path == [0]: # backtrached to the origin, only symmetrical status is left
                return (n,time()-start,None)    # No solution for this size
            
            # do backtraching updates
            isInPath[pos]=0
            path.pop()
            pos = path[-1]
        else:
            # initialize neighbours and sort by criterioScelta
            neighbor_list_pairs:list[tuple[int,int]]=getUnvisitedNeighboursWithCount(n, pos, isInPath)
            neighbor_list_pairs.sort(key = lambda neigPair: criterioScelta(n, neigPair[0], neigPair[1]))
        
        if neighbor_list_pairs==[]:
            isBackTrack = True # all neigbour where excluded
        else:
            pos=neighbor_list_pairs[0][0] # move to pos of first remaining neighbor
            path.append(pos)
            isInPath[pos]=1


if __name__ == '__main__':
    n=1000
    criterioScelta=eurMenoEntrantiDistCentroEuclidea
    timeOut=3600*24*7
    #nomeFile='./txt/provaiterativa2.txt'
    nomeFile=None

    numero,tempo,esito =percorsoCavalloIterativoNoGraph(n, timeOut, criterioScelta, nomeFile)
    print(numero,tempo,esito)
    if esito and not isValidSolution(n, esito):
        print(f'n={n} INVALID SOLUTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
