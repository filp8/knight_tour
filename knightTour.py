from time import time
from boardUtil import idxToCord,creaGrafo,make_cnt,update_cnt

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion

def percorsoCavalloIterativo(n,start,timeOut,criterioScelta):
    if n<3:
        return (n,time()-start,None)
    
    graph = creaGrafo(n)
    nelPath = [0]*(n*n)
    move_cnt = make_cnt(n)
    path = []
    stackNL = []
    pos = 0
    isBackTrack = False
    cnt_it = 0
    cnt_back = 0
    while True:
            print(f'n={n} iterazioni={cnt_it} backtrack={cnt_back}')
            if timeOut and time()-start>timeOut:
                return (n,time()-start,[])
            cnt_it+=1
            path.append(pos)
            nelPath[pos]=1
            deltalen=len(graph)-len(path)
            if not deltalen:
                return (n,time()-start,path)

            x,y = idxToCord(n,pos)

            if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
                if isBackTrack:
                    neighbor_list = stackNL.pop()
                    cnt_back+=1
                    
                    isBackTrack = False
                else:
                    neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
                    neighbor_list.sort(key = lambda neig: criterioScelta(n,neig,move_cnt))
                
                if neighbor_list==[]:
                    isBackTrack = True
                else:
                    pos = neighbor_list[0]
                    stackNL.append(neighbor_list[1:])
            else:
                isBackTrack = True

            if isBackTrack:
                path.pop()
                if path == [0]:
                    return (n, time()-start if start else None,None)
                else:
                    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
                    nelPath[pos]=0
                    pos = path.pop()
                
if __name__ == '__main__':
    print(percorsoCavalloIterativo(7,None,None,eurMenoEntrantiDistCentroEuclidea))


