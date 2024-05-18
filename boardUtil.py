def cordToIdx(n,x,y):
    return x+(y*n)

def idxToCord(n,i):
    x = i%n
    y = i//n
    return x,y

def creaGrafo(n):
    mosse_cavallo = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # (x,y)
    grafo = [[] for _ in range(n*n)]
    for x in range(n): # creo grafo
        for y in range(n):
            for mossa in mosse_cavallo:
                tx = x+mossa[0]
                ty = y+mossa[1]
                if n>tx>=0 and  n>ty>=0:
                    grafo[cordToIdx(n,x,y)].append(cordToIdx(n,tx,ty))
    return grafo

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
