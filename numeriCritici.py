import sys
sys.setrecursionlimit(1_100_000)

from time import time 
from knightTourTimeOut import percorsoCavalloTimeOut


def cercaNumeriCritici(fine,timeOut,inizio=5):
    numeri = []
    for n in range(inizio,fine):
        print(n)
        start = time()
        ret = percorsoCavalloTimeOut(n,start,timeOut)
        if type(ret)==int:
            numeri.append(ret)
    return numeri


if __name__ == '__main__':
    partenza = 0
    fine = 500
    timeOut = 1.0

    print(cercaNumeriCritici(fine,timeOut,partenza))
    # euristica base
    sec1 = [35, 36, 52, 63, 87, 93, 98, 99, 101, 106, 108, 109, 121, 125, 127, 141, 144, 145, 147, 152, 154, 157, 158, 161, 165, 166, 169, 173, 183, 184, 185, 189, 191, 193, 197, 199, 201, 205, 206, 209, 213, 215, 217, 219, 222, 223, 225, 227, 229, 230, 231, 234, 236, 237, 238, 239, 240, 241, 243, 247, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 263, 264, 265, 267, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 283, 284, 285, 287, 289, 291, 292, 294, 299]
    sec2 = [35, 36, 52, 63, 87, 93, 98, 99, 101, 106, 108, 109, 121, 125, 127, 141, 144, 145, 147, 152, 154, 157, 158, 161, 165, 166, 169, 173, 183, 185, 189, 191, 193, 197, 199, 201, 205, 206, 209, 213, 215, 217, 219, 222, 223, 225, 227, 229, 230, 231, 234, 236, 237, 238, 239, 240, 241, 243, 247, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 263, 264, 265, 267, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 283, 284, 285, 287, 289, 291, 292, 294, 299]
    # euristica  centro
