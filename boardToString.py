

def print_board(vett,n):
    sOut = ''
    cnt = 0
    for cas in vett:
        sOut+=str(cas)
        cnt+=1
        if cnt == n:
            sOut+='\n'
            cnt = 0
    print(sOut)
    return 

def save_board(vett,n,nomeFile,id,asTab=False,simboli=('0','1')):
    sOut = f'\n{id}\n\n'
    cnt = 0
    sep = '\t' if asTab else ''
    vuoto,pieno = simboli 
    for cas in vett:
        sOut += (pieno if cas else vuoto)+sep
        cnt+=1
        if cnt == n:
            sOut+='\n'
            cnt = 0
    with open(nomeFile, 'a') as f:
        f.write(sOut+'\n')
    return 

if __name__ == '__main__':
    vett = [0,1,0,1,0]*5
    save_board(vett,5,'prova_tab.tab',0,asTab=True,simboli = ['⬜','⬛'])
    
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