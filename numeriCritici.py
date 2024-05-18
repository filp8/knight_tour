import sys
sys.setrecursionlimit(1_100_000_000)

from time import time 
from knightTourTimeOut import percorsoCavalloTimeOut
from knightTourIterativo import percorsoCavalloIterativoTimeOut



def cercaNumeriCritici(fine,timeOut,inizio=5):
    numeri = []
    goal = []
    if inizio<5:
        inizio = 5
    for n in range(inizio,fine):
        start = time()
        #ret = percorsoCavalloTimeOut(n,start,timeOut)
        ret = percorsoCavalloIterativoTimeOut(n,start,timeOut)
        print(ret)

        if type(ret)==int:
            numeri.append(ret)
        else:
            goal.append(ret)
    return numeri,goal


if __name__ == '__main__':

    #print(percorsoCavalloIterativoTimeOut(1050,time(),10.0))
    #percorsoCavalloTimeOut(1050,time(),10.0)


    partenza = 1625
    fine = 1630
    timeOut = 15.0

    fail,goal = cercaNumeriCritici(fine,timeOut,partenza)
    print(goal)
    print(fail)

   
