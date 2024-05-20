import sys
sys.setrecursionlimit(1_100_000)

from time import time

from boardUtil import idxToCord,creaGrafo,update_cnt,make_cnt

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion


def hamiltonian_path(n, graph, pos, path, nelPath, move_cnt, criterioScelta):
    start=time()
    if n<3:
        return (n,time()-start,None)
    
    path.append(pos)
    nelPath[pos]=1
    deltalen=len(graph)-len(path)
    if not deltalen:
        return (n,time()-start,path)
    
    x,y = idxToCord(n,pos)

    if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
        neighbor_list.sort(key = lambda neig:criterioScelta(n,neig,move_cnt[neig]))
        for neighbor in neighbor_list:
            extended_path = hamiltonian_path(n,graph, neighbor, path,nelPath,move_cnt,criterioScelta,start)
            if extended_path: 
                return (n,time()-start,path)
        
    path.pop()
    nelPath[pos]=0
    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
    return (n,time()-start,None)

def percorsoCavalloRicorsivo(n, timeOut, criterioScelta):
    graf = creaGrafo(n)
    used = [0]*(n*n)
    move_cnt = make_cnt(n)
    sol = hamiltonian_path(n,graf,0,[],used,move_cnt,criterioScelta)
    return sol

if __name__ == '__main__':
    print(percorsoCavalloRicorsivo(300,None,None,eurMenoEntrantiDistCentroEuclidea))
