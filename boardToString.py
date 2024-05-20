

def print_board(vett,n):
    maxl = len(str(max(vett,key = lambda n: len(str(n)))))
    
    sOut = ''
    cnt = 0
    for cas in vett:
        sOut += f' {str(cas):^{maxl}s}'
        cnt+=1
        if cnt == n:
            sOut+='\n'
            cnt = 0
    print(sOut)
    return 

def print_board_pixel(n,path,vett):
    sOut = ''
    cnt = 0
    pos = path[-1]
    last = None
    lastlast = None
    if len(path)>1:
        last = path[-2]
    if len(path)>2:
        lastlast = path[-3]
    for i,cas in enumerate(vett):
        if i == pos:
            sOut+='🟥'
        elif i == last:
            sOut+='🟧'
        # elif i ==lastlast:
        #     sOut+='🟨'
        elif cas ==1:
            sOut+='⬛️'
        else:
            sOut+='⬜'
        cnt+=1
        if cnt == n:
            sOut+='\n'
            cnt = 0
    print(sOut)
    return 

def save_board(vett,n,pos,nomeFile,id,asTab=False,simboli=('0','1','\u265E')):
    sOut = f'\n{id}\n\n'
    cnt = 0
    sep = '\t' if asTab else ''
    vuoto,pieno,cavallo = simboli 
    for cas in vett:
        if cnt == pos:
            sOut+=cavallo
        else:
            sOut += (pieno if cas else vuoto)+sep
        cnt+=1
        if cnt%n == 0:
            sOut+='\n'
            
    with open(nomeFile, 'a') as f:
        f.write(sOut+'\n')
    return 

if __name__ == '__main__':
    vett = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
    save_board(vett,5,0,'./txt/prova.txt',0,asTab=False,simboli = ('⬜','⬛','⬛'))
    save_board(vett,5,0,'./txt/prova.txt',0,asTab=False,simboli = ('⬜','🟪','🟦'))
    save_board(vett,5,0,'./txt/prova.txt',0,asTab=False,simboli = ('⬜','⬛️','🟥'))
    
'''
https://symbl.cc/it/unicode-table/#miscellaneous-symbols
░ = U+2591 ombra leggera 
▒ = U+2592 ombra media
▓ = U+2593 ombra scura
█ = U+2588 full block
□ = U+25A1 quadrato bianco
♞ = U+265E cavallo
⬛ = U+2B1B grande quad nero
⬜ = U+2B1C grande quad bianco
⬤ = U+2B24 
'''