
from math import sqrt
from boardUtil import cordToIdx,idxToCord

def printCriterio():
    return

def dist_centro_euclidea(n,pos):
    x,y = idxToCord(n,pos)
    centro = n/2
    return sqrt((x-centro)**2+(y-centro)**2)

def eurMenoEntrantiDistCentro(n,neighbor,move_cnt):
    return (move_cnt[neighbor]*n)-dist_centro_euclidea(n,neighbor)

def eurMenoEntranti(n,neighbor,move_cnt):
    return move_cnt[neighbor]*n

def eurDistCentro(n,neighbor,move_cnt):
    return -dist_centro_euclidea(n,neighbor)

if __name__=='__main__':
    printCriterio()
