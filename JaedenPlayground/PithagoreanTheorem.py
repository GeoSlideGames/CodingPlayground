#TODO:add os package to clear the console after each major option
import math
from clearConsole import clearConsole
#TODO make a function to check if a variable is a string or a number
# then use it to check if the user inputs anything but a number and tell them to give a nummber 




def Pith():
    print #empty space to seprate
    print('1. Calculate for Slant Length')
    print('2. Calculate for Side Length')
    hypotonuseOrSide = float(input(''))
    
    clearConsole()
    print('Pithagreoas')                     
    if hypotonuseOrSide == 1:
        print #empty space to seprate
        print('Give Hight')
        hight = float(input(''))
        clearConsole()
        print('Pithagreoas')
        print(hight, '²') #empty space to seprate
        print('Give Lenght')
        length = float(input(''))
        
        clearConsole()
        print('Pithagreoas')
        print(hight,"²",' + ',length,"²")
        
        hightExponent = hight ** 2
        lengthExponent = length ** 2
        clearConsole()
        print('Pithagreoas')
        print(hight,'²',' + ','²',length,)
        print("the slant's length is ", math.sqrt(hightExponent + lengthExponent))

    elif hypotonuseOrSide == 2:
        print() #empty space to seprate
        print('Give Slant Hight')
        slant = float(input(''))
        print() #empty space to seprate
        print('Give Lenght')
        side = float(input(''))

        slantExponent = slant ** 2
        sideExponent = side ** 2
        print() #empty space to seprate
        print("the side's length is ",math.sqrt(slantExponent - sideExponent))