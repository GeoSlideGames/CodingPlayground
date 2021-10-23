#TODO:add os package to clear the console after each major option
import math
#TODO make a function to check if a variable is a string or a number
    # then use it to check if the user inputs anything but a number and tell them to give a nummber 

def Pith():
    print('1. Calculate for Hyptonuse Length')
    print('2. Calculate for Side Length')
    #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
    A = float(input(''))
    #TODO: clear here
    
    if A == 1:
        print('Give Hight')
        #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
        H = float(input(''))
        print('Give Lenght')
        #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
        L = float(input(''))

        #TODO: reprint hight and length
        print(math.sqrt(H*H+L*L),'=S')

    elif A == 2:
        print('Give Slant Hight')
        #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
        S = float(input(''))
        print('Give Lenght')
        #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
        L = float(input(''))

        print(math.sqrt(S*S-L*L),'=H')

