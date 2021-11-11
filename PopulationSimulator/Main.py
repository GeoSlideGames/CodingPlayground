import math
import random
import tkinter as tk
from typing import Text

def changeWaterLabel(WaterLabel,numOfWaterEntry):
    WaterLabel.config(text='') # clear label
    WaterLabel.config(text= numOfWaterEntry.get()) # set new label text

def changeFoodLabel(FoodLabel,numOfFoodEntry):
    FoodLabel.config(text='') # clear label
    FoodLabel.config(text= numOfFoodEntry.get()) # set new label text

def changeShelterLabel(ShelterLabel,numOfShelterEntry):
    ShelterLabel.config(text='') # clear label
    ShelterLabel.config(text= numOfShelterEntry.get()) # set new label text
    
def Resources():
    
    WaterVar = tk.StringVar()
    FoodVar = tk.StringVar()
    ShelterVar = tk.StringVar()

    numOfWaterEntry = tk.Entry(root, width=10,textvariable=WaterVar)
    numOfWaterEntry.grid(row=3, column=1)

    numOfFoodEntry = tk.Entry(root, width=10,textvariable=FoodVar)
    numOfFoodEntry.grid(row=3,column=2)

    numOfShelterEntry = tk.Entry(root, width=10,textvariable=ShelterVar)
    numOfShelterEntry.grid(row=3,column=3)

    WaterLabel = tk.Label(root,)
    WaterLabel.grid(row=2,column=1)
    FoodLabel = tk.Label(root,)
    FoodLabel.grid(row=2,column=2)
    ShelterLabel = tk.Label(root,)
    ShelterLabel.grid(row=2,column=3)

    WaterVar.trace_variable('w', changeWaterLabel(WaterLabel,numOfWaterEntry))
    FoodVar.trace_variable('w', changeWaterLabel(FoodLabel,numOfFoodEntry))
    ShelterVar.trace_variable('w', changeWaterLabel(ShelterLabel,numOfShelterEntry))

#Intalize Tkinter
root = tk.Tk()
root.title('Ecosystem Population Simulator')
root.geometry("750x500")


        

#def activate():

#advanceButton = tk.Button(root,padx=20,pady=20,text="activate", command=activate,).grid(row=4, column=2,)

Resources()
root.mainloop()

