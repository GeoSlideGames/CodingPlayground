import math
def Pith():
    print('1. Calculate for Hypotenuse Length')
    print('2. Calculate for Side Length')
    A = float(input(''))

    if A == 1:
        print('Give Height')
        H = float(input(''))
        print('Give Length')
        L = float(input(''))

        print(math.sqrt(H*H+L*L),'=S')

    elif A == 2:
        print('Give Slant Height')
        S = float(input(''))
        print('Give Length')
        L = float(input(''))

        print(math.sqrt(S*S-L*L),'=H')
