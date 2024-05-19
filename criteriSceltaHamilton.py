
from math import sqrt
from boardUtil import cordToIdx,idxToCord
from boardToString import print_board



def eurDistCentroEuclidea(n,pos,move_cnt):
    return -dist_centro_euclidea(n,pos)

def eurDistCentroManhattan(n,pos,move_cnt):
    return -dist_centro_manhattan(n,pos)


def eurMenoEntranti(n,pos,move_cnt):
    return move_cnt[pos]*n

def eurMenoEntrantiDistCentroEuclidea(n,pos,move_cnt):
    return (move_cnt[pos]*n)-dist_centro_euclidea(n,pos)

def eurMenoEntrantiDistCentroManhattan(n,pos,move_cnt):
    return (move_cnt[pos]*n)-dist_centro_manhattan(n,pos)



def dist_centro_euclidea(n,pos,move_cnt):
    x,y = idxToCord(n,pos)
    centro = n/2
    return sqrt((x-centro)**2+(y-centro)**2)

def dist_centro_manhattan(n,pos):
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

def printCriterio(n,criterio):
    boardOut=[]
    for y in range(n):
        for x in range(n):
            boardOut.append(criterio(n,cordToIdx(n,x,y),None))
    print_board(boardOut,n)
    return boardOut


if __name__=='__main__':
    printCriterio(5,eurDistCentroManhattan)
