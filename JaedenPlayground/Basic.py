#do you need this file anymore if you are using SourcedBasic now?



#TODO:add os package to clear the console after each major option
def calculator():

    A = float(input("Input a Number"))
    #TODO:add clear here 
    #TODO:add a reprint to show your chosen number
    print('choose an opperator, Please')
    print('1. +')
    print('2. -')
    print('3. *')
    print('4. /')
    print('5. %')
    C = float(input(''))
    #TODO: add clear here
    #TODO: add a number reprint + symbol reprint to show current number
    B = float(input("Input a Second Number"))
    #This is where it calculates.
    #TODO: print the entire formula here ex: 2 + 3 ex: 56 / 2
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
    #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
    E = float(input(''))
    
    if E == 1:
        calculator()
    elif E == 2:
        print('Sure Thing!')