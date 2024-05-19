from time import time

from boardUtil import idxToCord,creaGrafo,make_cnt,update_cnt
from boardToString import save_board

from criteriSceltaHamilton import eurDistCentroEuclidea, eurDistCentroManhattan, eurDistCentroOnion, eurMenoEntranti,  \
                                  eurMenoEntrantiDistCentroEuclidea, eurMenoEntrantiDistCentroManhattan, eurMenoEntrantiDistCentroOnion

def percorsoCavalloIterativoSave(n,stepSave,nomeFile,asTab,simboli,criterioScelta,id=0):
    if n<3:
        return (n,0,None)
    
    start = time()
    graph = creaGrafo(n)
    nelPath = [0]*(n*n)
    move_cnt = make_cnt(n)
    path = []
    stackNL = []
    pos = 0
    isBackTrack = False
    while True:
            path.append(pos)
            nelPath[pos]=1
            if id%stepSave==0:
                save_board(nelPath,n,pos,nomeFile,id,asTab,simboli)
                print(id)
            id+=1

            deltalen=len(graph)-len(path)
            if not deltalen:
                return (n,time()-start,path)

            x,y = idxToCord(n,pos)
            doBackT = update_cnt(n,x,y,move_cnt,nelPath,dec=True)
            if not doBackT or deltalen == 1:
                
                if not isBackTrack:
                    if path == [0]:
                        return None
                    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
                    nelPath[pos]=0
                    path.pop()
                    pos = path.pop()
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

                

                



if __name__ == '__main__':
    print(percorsoCavalloIterativoSave(7,1,'./txt/provaiterativa2.txt',False,('⬜','⬛️','🟥'),eurMenoEntrantiDistCentroEuclidea))


