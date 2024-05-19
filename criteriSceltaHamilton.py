
from math import sqrt
from boardUtil import cordToIdx,idxToCord
from boardToString import print_board

def printCriterio(n,criterio):
    boardOut=[]
    for y in range(n):
        for x in range(n):
            boardOut.append(criterio(n,cordToIdx(n,x,y),None))
    print_board(boardOut,n)
    return boardOut

def dist_centro_euclidea(n,pos,move_cnt):
    x,y = idxToCord(n,pos)
    centro = n/2
    return sqrt((x-centro)**2+(y-centro)**2)

def eurMenoEntrantiDistCentroEuclidea(n,pos,move_cnt):
    return (move_cnt[pos]*n)-dist_centro_euclidea(n,pos,move_cnt)

def eurMenoEntranti(n,pos,move_cnt):
    return move_cnt[pos]*n

def eurDistCentroEuclidea(n,pos,move_cnt):
    return -dist_centro_euclidea(n,pos,move_cnt)

def eurDistManhattan(n,pos,move_cnt):
    return -dist_centro_manhattan(n,pos,move_cnt)

def eurMenoEntrantiDistCentroManhattan(n,pos,move_cnt):
    return (move_cnt[pos]*n)-dist_centro_manhattan(n,pos,move_cnt)

def eurMenoEntrantiDistCentroF(n,pos,move_cnt):
    return (move_cnt[pos]*n)-dist_centro_f(n,pos,move_cnt)

def eurDistCentroF(n,pos,move_cnt):
    return -dist_centro_f(n,pos,move_cnt)


def dist_centro_manhattan(n,pos,move_cnt):
    x,y = idxToCord(n,pos)
    centro = ((n+1)//2)-1
    xdist = abs(centro-x)
    ydist = abs(centro-y)
    if n%2 == 0:
        if x<=centro:
            xdist+=1
        if y<=centro:
            ydist+=1
    return  xdist+ydist

def dist_centro_f(n,pos,move_cnt):
    x,y = idxToCord(n,pos)
    centro = ((n+1)//2)-1
    xdist = abs(centro-x)
    ydist = abs(centro-y)
    if n%2==0:
        if x<=centro:
            xdist+=1
        if y<=centro:
            ydist+=1

    return  max(xdist,ydist)

if __name__=='__main__':
    printCriterio(6,dist_centro_manhattan)
