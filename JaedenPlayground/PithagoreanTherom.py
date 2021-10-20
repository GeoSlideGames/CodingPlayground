import math
def Pith():
    print('1. H^2 + L^2 = S^2')
    print('2. S^2 - L^2 = H^2')

    A = float(input('Select option 1 or 2:'))

    if A == 1:
        H = float(input('Give Hight:'))
        L = float(input('Give Lenght:'))
        print(math.sqrt(H*H+L*L),'=S')
        print()
    elif A == 2:
        S = float(input('Give Slant Hight:'))
        L = float(input('Give Lenght:'))
        print(math.sqrt(S*S-L*L),'=H')
        print()
Pith()
