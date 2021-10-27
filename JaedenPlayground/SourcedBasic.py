#TODO:add os package to clear the console after each major option
def calculator():
    #TODO make a function to check if a variable is a string or a number
    # then use it to check if the user inputs anything but a number and tell them to give a nummber  
    print() #empty space to seprate
    print('Input a Number')
    num1 = float(input(''))
    #TODO:add clear here
    #TODO:add a reprint to show your chosen number
    print() #empty space to seprate
    print('choose an opperator, Please')
    print('1. +')
    print('2. -')
    print('3. *')
    print('4. /')
    print('5. %')
    operator = float(input(''))
    #TODO: add clear here
    #TODO: add a number reprint + symbol reprint to show current number
    print() #empty space to seprate
    print('Input a Second Number')
    num2 = float(input(''))
    #TODO: print the entire formula here ex: 2 + 3 ex: 56 / 2
    #This is where it calculates.
    print() #empty space to seprate
    if operator == 1:
        print(num1 + num2)
        
    elif operator == 2:
        print(num1 - num2)
        
    elif operator == 3:
        print(num1 * num2)
        
    elif operator == 4:
        print(num1 / num2)
        
    elif operator == 5:
        print(num1 % num2)