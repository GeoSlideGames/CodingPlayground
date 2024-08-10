from ClearConsole import clearConsole

def calculation():
    #TODO make a function to check if a variable is a string or a number
    # then use it to check if the user inputs anything but a number and tell them to give a number  
    clearConsole()
    print('Basic Math')
    
    print() #empty space to separate
    print('Input a Number')
    num1 = float(input(''))
    clearConsole()
    print('Basic Math')
    print(num1)

    print() #empty space to separate
    print('choose an operator, Please')
    print('Type "1" for addition')
    print('Type "2" for subtraction')
    print('Type "3" for multiplication')
    print('Type "4" for division')
    print('Type "5" for remainder')
    operator = input('')
    if operator == '1':
        operatorSymbol = '+'
    elif operator == '2':
        operatorSymbol = '-'        
    elif operator == '3':
        operatorSymbol = '*'          
    elif operator == '4':
        operatorSymbol = '/'        
    elif operator == '5':
        operatorSymbol = '%'
    clearConsole()
    print('Basic Math')
    print(num1,' ',operatorSymbol)
    
    print() #empty space to separate
    print('Input a Second Number')
    num2 = float(input(''))
    clearConsole()
    print('Basic Math')
    
    #TODO: print the entire formula here ex: 2 + 3 ex: 56 / 2
    #This is where it calculates.
    
    if operator == '1':
        print(num1,'',operatorSymbol,'',num2,'=', num1 + num2)
        
    elif operator == '2':
        print(num1,'',operatorSymbol,'',num2,'=', num1 - num2)
        
    elif operator == '3':
        print(num1,'',operatorSymbol,'',num2,'=', num1 * num2)
        
    elif operator == '4':
        print(num1,'',operatorSymbol,'',num2,'=', num1 / num2)
        
    elif operator == '5':
        print(num1,'',operatorSymbol,'',num2,'=', num1 % num2)
