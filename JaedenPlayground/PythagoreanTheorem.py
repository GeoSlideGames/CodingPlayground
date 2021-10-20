import math
def Pith():
    print('1. Calculate for Hyptonuse Length')
    print('2. Calculate for Side Length')
    A = float(input(''))

    if A == 1:
        print('Give Hight')
        H = float(input(''))
        print('Give Lenght')
        L = float(input(''))

        print(math.sqrt(H*H+L*L),'=S')

    elif A == 2:
        print('Give Slant Hight')
        S = float(input(''))
        print('Give Lenght')
        L = float(input(''))

        print(math.sqrt(S*S-L*L),'=H')
