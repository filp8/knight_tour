from time import time
from boardUtil import idxToCord,creaGrafo,make_cnt,update_cnt
from criteriSceltaHamilton import eurDistCentro,eurMenoEntrantiDistCentro


def percorsoCavalloIterativoTimeOut(n,start,timeOut,criterioScelta):
    if n<3:
        return None
    graph = creaGrafo(n)
    nelPath = [0]*(n*n)
    move_cnt = make_cnt(n)
    path = []
    stackNL = []
    pos = 0
    isBackTrack = False
    while True:
            temp = time()-start
            if timeOut and temp>timeOut:
                return n
            path.append(pos)
            nelPath[pos]=1
            deltalen=len(graph)-len(path)
            if not deltalen:
                return (n,temp)

            x,y = idxToCord(n,pos)

            if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
                if isBackTrack:
                    neighbor_list = stackNL.pop()
                    isBackTrack = False
                else:
                    neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
                    neighbor_list.sort(key = lambda neig: criterioScelta(n,neig,move_cnt))
                
                if neighbor_list==[]:
                    isBackTrack = True
                else:
                    pos = neighbor_list[0]
                    stackNL.append(neighbor_list[1:])
            else:
                isBackTrack = True

            if isBackTrack:
                path.pop()
                if path == [0]:
                    return (n,temp)
                else:
                    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
                    nelPath[pos]=0
                    pos = path.pop()
                

#TODO quando metto una casella a 1 nel vettore caratteristico nelPath mi devo assicurare che tutti gli zero che puntano all'uno appena messo abbiamo almeno un altro zero su cui andare 
if __name__ == '__main__':
    print(percorsoCavalloIterativoTimeOut(4000,time(),None,eurMenoEntrantiDistCentro))


