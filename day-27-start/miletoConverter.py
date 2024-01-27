from tkinter import * 

mainWindow = Tk()
mainWindow.title("Mile to Kilometers Converter")
mainWindow.minsize(width=100, height=100)
mainWindow.config(padx=10, pady=10)

labelOne = Label(width=20, text="Miles", font=("Arial", 10, "italic"))
labelOne.grid(column=3,row=1)

input = Entry(width=(25))
input.grid(column=2, row=1)
input.insert(END,string= "Enter Miles Here..." )

labelTwo = Label(text="is equal to ")
labelTwo.grid(column=2, row=2)
answerLabel = Label(text= "Km")
answerLabel.grid(column=3, row=2)
def button_Clicked():
    miles = input.get()
    kilo = float(miles) * 1.6
    answerLabel.config(text=str(round(kilo))+ " Kilometes")

calcButton = Button(width=20, text="Calculate", command= button_Clicked)
calcButton.grid(column=2, row=3)

mainWindow.mainloop()