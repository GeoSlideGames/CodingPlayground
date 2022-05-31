import random as RD

#print binngo letter and number
number = RD.randint(1,14)
letternum = RD.randint(1,5)
if letternum == 1:
    letter = "B"
elif letternum == 2:
    letter = "I"
elif letternum == 3:
    letter = "N"
elif letternum == 4:
    letter = "G"
elif letternum == 5:
    letter = "O"
print(letter,number)