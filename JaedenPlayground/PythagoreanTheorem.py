#TODO:add os package to clear the console after each major option
import math
from clearConsole import clearConsole
#TODO make a function to check if a variable is a string or a number
# then use it to check if the user inputs anything but a number and tell them to give a nummber 




def Pyth():
    clearConsole()
    print('Pythagorean Theorem')
    print()
    print('1. Calculate for the Slant')
    print('2. Calculate for a Side')
    SlantOrSide = float(input(''))

    if  SlantOrSide == 1:
        clearConsole()
        print('Pythagorean Theorem')     
        print()
        print('Height² + Length² = Slant²')
        print()
        print('Give Hight')
        height = float(input(''))
        clearConsole()

        print('Pythagorean Theorem')
        print()
        print(height,'² + Length² = Slant²')
        print()
        print('Give Length')
        length = float(input(''))
                
        clearConsole()
        heightExponent = height ** 2
        lengthExponent = length ** 2
        print('Pythagorean Theorem')
        print()
        print(height,'² + ',length,'² = ',math.sqrt(heightExponent + lengthExponent),'²')

    elif SlantOrSide == 2:
        clearConsole()
        print('Pythagorean Theorem')     
        print()
        print('Slant² - Length² = Height²')
        print()
        print('Give Slant')
        slant = float(input(''))

        clearConsole()
        print('Pythagorean Theorem')
        print()
        print(slant,'² - Length² = Height²')
        print()
        print('Give Length')
        length = float(input(''))
        
        clearConsole()
        slantExponent = slant ** 2
        lengthExponent = length ** 2
        print('Pythagorean Theorem')
        print()
        print(slant,'² - ',length,'² = ',math.sqrt(slantExponent - lengthExponent),'²')