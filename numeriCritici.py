from time import time 

from knightTour import percorsoCavalloIterativo
from knightTourNoBacktrack import percorsoCavalloNoBack
from knightTourRicorsivo import percorsoCavalloRicorsivo

from criteriSceltaHamilton import eurDistCentro,eurMenoEntrantiDistCentro,eurMenoEntranti


def cercaNumeriCritici(inizio,fine,step,timeOut,algoritmo,criterioScelta):
    fail = []
    gooal = []
    if inizio<5:
        inizio = 5
    for n in range(inizio,fine,step):
        print(n)
        start = time()
        ret = algoritmo(n,start,timeOut,criterioScelta)
        print(ret)
        if ret==None:
            fail.append(n)
        else:
            gooal.append(n)
    return fail,gooal


if __name__ == '__main__':

    inizio = 0
    fine = 10
    step = 1
    timeOut = 1000.0

    fail,gooal = cercaNumeriCritici(inizio,fine,step,timeOut,percorsoCavalloRicorsivo,eurMenoEntrantiDistCentro)

    print(gooal)
    print()
    print(fail)
    print(f'\n\n inizio:{inizio}     fine:{fine}     step:{step}     timeOut:{timeOut}')
    print(f'\n goal:{len(gooal)}')

    print(f'\n fail:{len(fail)}')

   
