import sys
sys.setrecursionlimit(1_100_000)
from math import sqrt
from boardUtil import idxToCord,creaGrafo,update_cnt,make_cnt
from criteriSceltaHamilton import eurDistCentro,eurMenoEntrantiDistCentro


def hamiltonian_path(n,graph, pos, path, nelPath, move_cnt,criterioScelta):
    path.append(pos)
    nelPath[pos]=1
    deltalen=len(graph)-len(path)
    if not deltalen:
        return path
    
    x,y = idxToCord(n,pos)

    if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
#        neighbor_list.sort(key = lambda neig: (move_cnt[neig]*n)-dist_centro(n,neig))
        neighbor_list.sort(key = lambda neig:criterioScelta(n,neig,move_cnt))
        for neighbor in neighbor_list:
            extended_path = hamiltonian_path(n,graph, neighbor, path,nelPath,move_cnt,criterioScelta)
            if extended_path: 
                return extended_path
        
    path.pop()
    nelPath[pos]=0
    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
    return None

def percorsoCavalloRicorsivo(n,criterioScelta):
    graf = creaGrafo(n)
    used = [0]*(n*n)
    move_cnt = make_cnt(n)
    sol = hamiltonian_path(n,graf,0,[],used,move_cnt,criterioScelta)
    return sol

if __name__ == '__main__':
    print(percorsoCavalloRicorsivo(300,eurMenoEntrantiDistCentro))
