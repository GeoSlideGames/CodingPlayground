#TODO: find a way to add multiple answer to the if's
#TODO: make a function to check if a variable is a string or a number
# then use it to check if the user inputs anything but a number and tell them to give a number 
from PythagoreanTheorem import Pyth
from BasicFunctions import calculation
from ClearConsole import clearConsole


def Choice():
    clearConsole()
    print('Type 1 For a Basic Calculator')
    print('Type 2 to Calculate for Pythagorean Theorem')
    #print('And 3 If you want to Calculate for Tan')
    
    TypeOFQuestion = float(input(''))
    

    if TypeOFQuestion == 1:
        calculation()

    elif TypeOFQuestion == 2:
        Pyth()
    
    #elif A == 3:
        #C = float(input('Solve for angle:1, Opp:2 or Adj:3 '))
        
        #if C == 1:
            #
        #elif C == 2:
            #
        #elif C == 3:
    print() #empty space to separate
    print('To Continue with MORE Math! 1')
    print('Alternatively, to End Calculations, 2')
    

    ContinuationChoice = float(input(''))

    if ContinuationChoice == 1:
        Choice()

    elif ContinuationChoice == 2:
        clearConsole()
        print() #empty space to separate
        print() #empty space to separate
        print('Goodbye Then! :)')
        print() #empty space to separate
        print() #empty space to separate
Choice()