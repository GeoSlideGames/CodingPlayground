import tkinter as tk

#Intalize Tkinter
def changeWaterLabel(*args):
    WaterLabel.config(text='') # clear label
    WaterLabel.config(text= "Water = " + numOfWaterEntry.get()) # set new label text

def changeFoodLabel(*args):
    FoodLabel.config(text='') # clear label
    FoodLabel.config(text= "Food = " + numOfFoodEntry.get()) # set new label text

def changeShelterLabel(*args):
    ShelterLabel.config(text='') # clear label
    ShelterLabel.config(text= "Shelter = " + numOfShelterEntry.get()) # set new label text
    
def StartTkinter():
    root = tk.Tk()
    root.title('Ecosystem Population Simulator')

    #set traceable variables
    WaterVar = tk.StringVar()
    FoodVar = tk.StringVar()
    ShelterVar = tk.StringVar()
    #create entry boxes
    numOfWaterEntry = tk.Entry(root, width=10,textvariable=WaterVar)
    numOfFoodEntry = tk.Entry(root, width=10,textvariable=FoodVar)
    numOfShelterEntry = tk.Entry(root, width=10,textvariable=ShelterVar)
    #create changeable labels
    WaterLabel = tk.Label(root,text="Water = 0")
    FoodLabel = tk.Label(root,text="Food = 0")
    ShelterLabel = tk.Label(root,text="Shelter = 0")
    
    #detect when entry boxes value changes
    WaterVar.trace('w', changeWaterLabel)
    FoodVar.trace('w', changeFoodLabel)
    ShelterVar.trace('w', changeShelterLabel)

    #place everything on screen
    numOfWaterEntry.grid(row=3, column=1)
    numOfFoodEntry.grid(row=3,column=2)
    numOfShelterEntry.grid(row=3,column=3)
    WaterLabel.grid(row=2,column=1)
    FoodLabel.grid(row=2,column=2)
    ShelterLabel.grid(row=2,column=3)
    #start
    root.mainloop()


StartTkinter()

