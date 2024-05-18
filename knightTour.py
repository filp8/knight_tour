import sys
sys.setrecursionlimit(1_100_000)
from math import sqrt
from boardUtil import cordToIdx,idxToCord,creaGrafo

def make_cnt(n:int)->list[int]:
    cnt = [0]*(n*n)
    for y in range(n):
        for x in range(n):
            update_cnt(n,x,y,cnt,None,False)
    return cnt

def update_cnt(n:int, x:int, y:int, cnt:list[int],nelPath:list[int],dec:bool)->bool:
    rev = False
    mosse_cavallo = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # (x,y)
    for mossa in mosse_cavallo:
                tx = x+mossa[0]
                ty = y+mossa[1]
                if n>tx>=0 and  n>ty>=0:
                    t_idx = cordToIdx(n,tx,ty)
                    if dec:
                        cnt[t_idx]-=1
                        if cnt[t_idx]==0 and nelPath[t_idx]==0:
                            rev = True
                    else:
                        cnt[t_idx]+=1
    return rev

def dist_centro(n:int, pos:int)->float:
    x,y = idxToCord(n,pos)
    centro = n/2
    return sqrt((x-centro)**2+(y-centro)**2)

def hamiltonian_path(n:int, graph, pos:int, path:list[int], nelPath:list[int], move_cnt:list[int])->list[int]:
    path.append(pos)
    nelPath[pos]=1
    deltalen=len(graph)-len(path)
    if not deltalen:
        return path
    
    x,y = idxToCord(n,pos)

    if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
#        neighbor_list.sort(key = lambda neig: (move_cnt[neig]*n)-dist_centro(n,neig))
        neighbor_list.sort(key = lambda neig:-dist_centro(n,neig))
        for neighbor in neighbor_list:
            extended_path = hamiltonian_path(n,graph, neighbor, path,nelPath,move_cnt)
            if extended_path: 
                return extended_path
        
    path.pop()
    nelPath[pos]=0
    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
    return None

def percorsoCavallo(n:int)->list[int]:
    graf = creaGrafo(n)
    used:list[int] = [0]*(n*n)
    move_cnt:list[int] = make_cnt(n)
    sol:list[int] = hamiltonian_path(n,graf,0,[],used,move_cnt)
    return sol



#TODO quando metto una casella a 1 nel vettore caratteristico nelPath mi devo assicurare che tutti gli zero che puntano all'uno appena messo abbiamo almeno un altro zero su cui andare 
if __name__ == '__main__':
    print(percorsoCavallo(300))
    #print(percorsoCavallo(35))