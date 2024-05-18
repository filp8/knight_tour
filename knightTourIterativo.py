import sys
sys.setrecursionlimit(1_100_000)
from time import time
from math import sqrt
from boardUtil import cordToIdx,idxToCord,creaGrafo

def make_cnt(n):
    cnt = [0]*(n*n)
    for y in range(n):
        for x in range(n):
            update_cnt(n,x,y,cnt,None,False)
    return cnt

def update_cnt(n,x,y,cnt,nelPath,dec):
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

def dist_centro(n,pos):
    x,y = idxToCord(n,pos)
    centro = n/2
    return sqrt((x-centro)**2+(y-centro)**2)



def percorsoCavalloIterativoTimeOut(n,start,timeOut):
    graph = creaGrafo(n)
    nelPath = [0]*(n*n)
    move_cnt = make_cnt(n)
    path = []
    pos = 0
    last = None
    bad_move = [[] for _ in range(n*n)]
    while True:
            temp = time()-start
            if temp>timeOut:
                return n
            path.append(pos)
            nelPath[pos]=1
            deltalen=len(graph)-len(path)
            if not deltalen:
                return (n,temp)

            x,y = idxToCord(n,pos)
            if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
                neighbor_list = [n for n in graph[pos] if nelPath[n]==0 and (n not in bad_move[pos])]
                neighbor_list.sort(key = lambda neig: (move_cnt[neig]*n)-dist_centro(n,neig))
                if neighbor_list==[]:
                    path.pop()
                    nelPath[pos]=0
                    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
                    pos = last
                    last = path[-2]
                else:
                    last = pos
                    pos = neighbor_list[0]
            else:
                path.pop()
                nelPath[pos]=0
                update_cnt(n,x,y,move_cnt,nelPath,dec=False)
                bad_move[last].append(pos)
                pos = last
    return path


#TODO quando metto una casella a 1 nel vettore caratteristico nelPath mi devo assicurare che tutti gli zero che puntano all'uno appena messo abbiamo almeno un altro zero su cui andare 
if __name__ == '__main__':
    print(percorsoCavalloIterativoTimeOut(660,time(),100.0))
    #percorsoCavalloTimeOut(35,time(),1.0)


