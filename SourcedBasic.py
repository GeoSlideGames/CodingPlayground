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

calculator()
#Calculator() makes it start the process.