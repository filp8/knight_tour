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

def getMosseCavallo()->list[tuple[int,int]]:
    return [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # (x,y)

def update_cnt(n,x,y,cnt,nelPath,dec):
    rev = False
    mosse_cavallo:list[tuple[int,int]] = getMosseCavallo()
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

def isValidSolution(n:int, posSequence:list[int])->bool:
    posCount = len(posSequence)
    if posCount != n*n:
        print(f'n={n}: invalid posCount={posCount}, n*n={n*n}')
        print(posSequence)
        return False
    for iPos, pos in enumerate(posSequence):
        if iPos>0:
            xFrom, yFrom = idxToCord(n, posSequence[iPos-1])
            xTo, yTo = idxToCord(n, pos)
            absDx=abs(xFrom-xTo)
            absDy=abs(yFrom-yTo)
            if absDx+absDy != 3:
                print(posSequence)
                print(f'n={n}: invalid move! pos={pos} from=({xFrom},{yFrom}), to=({xTo},{yTo})')
                return False
    return True