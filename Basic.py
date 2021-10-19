def calculator():
    A = float(input("Input a Number"))
    
    print('choose an opperator, Please')
    print('1. +')
    print('2. -')
    print('3. *')
    print('4. /')
    print('5. %')
    
    C = float(input(''))
    B = float(input("Input a Second Number"))
    #This is where it calculates.
    if C == 1:
        print(A+B)
        
    elif C == 2:
        print(A-B)
        
    elif C == 3:
        print(A*B)
        
    elif C == 4:
        print(A/B)
        
    elif C == 5:
        print(A%B)
    
    print('1. Calculate Again')
    print('2. End Calculation Process')
    
    E = float(input(''))
    
    if E == 1:
        calculator()
    elif E == 2:
        print('Sure Thing!')
        
calculator()
#Calculator() makes it start the process.