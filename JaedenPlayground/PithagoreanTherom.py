def Pith():
    print('1. H^2 + L^2 = S^2')
    print('2. S^2 - L^2 = H^2')
    print('3. S^2 - H^2 = L^2')

    A = float(input('Select option 1,2 or 3'))

    if A == 1:
        H = float(input('Give Hight:'))
        L = float(input('Give Lenght:'))
        print(H*H+L*L,'=S^2')
        print()
    elif A == 2:
        S = float(input('Give Slant Hight:'))
        L = float(input('Give Lenght:'))
        print(S*S-L*L,'=H^2')
        print()
    elif A == 3:
        S = float(input('Give Slant Hight:'))
        H = float(input('Give Hight:'))
        
        print(S*S-H*H,'=L^2')
        print()
Pith()