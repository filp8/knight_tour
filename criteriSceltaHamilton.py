from math import sqrt

from boardUtil import cordToIdx,idxToCord
from boardToString import print_board



def eurDistCentroEuclidea(n:int, pos:int, neighCount:int)->float:
    return -dist_centro_euclidea(n,pos)

def eurDistCentroManhattan(n:int, pos:int, neighCount:int)->float:
    return -dist_centro_manhattan(n,pos)

def eurDistCentroOnion(n:int, pos:int, neighCount:int)->float:
    return -dist_centro_onion(n,pos)


def eurMenoEntranti(n:int, pos:int, neighCount:int)->float:
    return neighCount

def eurMenoEntrantiDistCentroEuclidea(n:int, pos:int, neighCount:int)->float:
    return (neighCount*n)-dist_centro_euclidea(n,pos)

def eurMenoEntrantiDistCentroManhattan(n:int, pos:int, neighCount:int)->float:
    return (neighCount*n)-dist_centro_manhattan(n,pos)

def eurMenoEntrantiDistCentroOnion(n:int, pos:int, neighCount:int)->float:
    return (neighCount*n)-dist_centro_onion(n,pos)



def dist_centro_euclidea(n:int ,pos:int )->float:
    x,y = idxToCord(n,pos)
    centro = n/2
    return sqrt((x-centro)**2+(y-centro)**2)

def dist_centro_manhattan(n:int ,pos:int )->float:
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

def dist_centro_onion(n:int ,pos:int )->float:
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

def printCriterio(n:int, criterio):
    boardOut=[]
    for y in range(n):
        for x in range(n):
            boardOut.append(criterio(n,cordToIdx(n,x,y),None))
    print_board(boardOut,n)
    return boardOut


if __name__=='__main__':
    printCriterio(5,eurDistCentroManhattan)
