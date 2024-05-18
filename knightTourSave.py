import sys
sys.setrecursionlimit(1_100_000)

from boardUtil import idxToCord,creaGrafo
from boardToString import save_board
from knightTourTimeOut import update_cnt,dist_centro,make_cnt

def hamiltonian_path(n,graph, pos, path, nelPath, move_cnt,nomeFile,asTab,simboli,id=0):
    path.append(pos)
    nelPath[pos]=1
    step = 1000 # salva una board ogni step mosse
    if id%step==0:
        save_board(nelPath,n,pos,nomeFile,id,asTab,simboli = simboli)
        print(id)
    #make_img_from_board(nelPath,n,1000,nomeFile+str(id))
    id+=1
    
    deltalen=len(graph)-len(path)
    if not deltalen:
        return path
    
    x,y = idxToCord(n,pos)

    if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
        neighbor_list.sort(key = lambda neig: (move_cnt[neig]*n)-dist_centro(n,neig))
        for neighbor in neighbor_list:
            extended_path = hamiltonian_path(n,graph, neighbor, path,nelPath,move_cnt,nomeFile,asTab,simboli,id)
            if extended_path: 
                return extended_path
    path.pop()
    nelPath[pos]=0
    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
    return None

def percorsoCavallo(n,asTab=False,simboli=['0','1','2']):
    graf = creaGrafo(n)
    used = [0]*(n*n)
    move_cnt = make_cnt(n)
    nomeRicerca = './txt/('+str(n)+'*'+str(n)+')ricerca.'
    nomeRicerca += 'tab' if asTab else 'txt'
    with open(nomeRicerca, 'w') as f:
        f.write('\n')
    sol = hamiltonian_path(n,graf,0,[],used,move_cnt,nomeRicerca,asTab=asTab,simboli=simboli,id=0)
    save_board(used,n,None,nomeRicerca,None,asTab,simboli = simboli)
    return sol

#TODO quando metto una casella a 1 nel vettore caratteristico nelPath mi devo assicurare che tutti gli zero che puntano all'uno appena messo abbiamo almeno un altro zero su cui andare 
if __name__ == '__main__':
    #percorsoCavallo(378,asTab=False,simboli = ['⬜','⬛️','🟥'])
    percorsoCavallo(378,asTab=False,simboli = ['0','1','2'])

    #percorsoCavallo(35,asTab=False)


