

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

def save_board(vett,n,nomeFile):
    sOut = ''
    cnt = 0
    for cas in vett:
        sOut+=str(cas)
        cnt+=1
        if cnt == n:
            sOut+='\n'
            cnt = 0
    with open(nomeFile, 'a') as f:
        f.write(sOut+'\n\n')
    return 