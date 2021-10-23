#TODO:add os package to clear the console after each major option
def calculator():
    #TODO make a function to check if a variable is a string or a number
    # then use it to check if the user inputs anything but a number and tell them to give a nummber  
    print('Input a Number')
    #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
    A = float(input(''))
    #TODO:add clear here
    #TODO:add a reprint to show your chosen number
    print('choose an opperator, Please')
    print('1. +')
    print('2. -')
    print('3. *')
    print('4. /')
    print('5. %')
    #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
    C = float(input(''))
    #TODO: add clear here
    #TODO: add a number reprint + symbol reprint to show current number
    print('Input a Second Number')
    #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
    B = float(input(''))
    #TODO: print the entire formula here ex: 2 + 3 ex: 56 / 2
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
#Calculator() makes it start the process.