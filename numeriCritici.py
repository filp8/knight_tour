from time import time 

from knightTour import percorsoCavalloIterativo
from knightTourNoBacktrack import percorsoCavalloNoBack
from knightTourRicorsivo import percorsoCavalloRicorsivo

from criteriSceltaHamilton import eurDistCentro,eurMenoEntrantiDistCentro,eurMenoEntranti


def cercaNumeriCritici(inizio,fine,step,timeOut,algoritmo,criterioScelta):
    numeri = []
    goal = []
    if inizio<5:
        inizio = 5
    for n in range(inizio,fine,step):
        start = time()
        ret = algoritmo(n,start,timeOut,criterioScelta)
        print(ret)
        if type(ret)==int:
            numeri.append(ret)
        else:
            goal.append(ret)
    return numeri,goal


if __name__ == '__main__':

    inizio = 0
    fine = 400
    step = 1
    timeOut = 1000.0

    fail,goal = cercaNumeriCritici(inizio,fine,step,timeOut,percorsoCavalloIterativo,eurMenoEntrantiDistCentro)

    print(f'\n\n inizio:{inizio}     fine:{fine}     step:{step}     timeOut:{timeOut}')
    print(f'\n goal:{len(goal)}')
    print(f'\n fail:{len(fail)}')

   
