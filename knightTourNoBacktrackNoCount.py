from time import time

from boardUtil import idxToCord,creaGrafo,make_cnt,update_cnt

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion


def percorsoCavalloNoBackNoCount(n,start,timeOut,criterioScelta):
    if n<3:
        return (n,time()-start,None)
        
    graph = creaGrafo(n)
    nelPath = [0]*(n*n)
    path = []
    pos = 0
    while True:
        if timeOut and time()-start>timeOut:
            return (n,time()-start,[])
        
        path.append(pos)
        nelPath[pos]=1

        if not (len(graph)-len(path)):
            return (n,time()-start,path)

        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
        neighbor_list.sort(key = lambda neig: criterioScelta(n,neig,None))
        
        if neighbor_list==[]:
            return (n,time()-start,[])
        else:
            pos = neighbor_list[0]
                
                
                
if __name__ == '__main__':
    print(percorsoCavalloNoBackNoCount(4000,time(),None,eurDistCentroManhattan))


