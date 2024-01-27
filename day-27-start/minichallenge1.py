from tkinter import * 

mainWindow = Tk()
mainWindow.title("Challenge 1")
mainWindow.minsize(width=500,height=300)
mainWindow.config(padx= 100, pady=100)
#Padding adds space around each widget. Can be done to all or each individual widget. 
labelOne = Label(text="Label 1", font=("Arial", 20))
labelOne.grid(column=0, row=0)


buttonOne = Button(text="Click me")
buttonOne.grid(column=2,row=1)


buttonTwo = Button(text="Click me too")
buttonTwo.grid(column=3,row=0)


input = Entry(width=15)
input.insert(END, string="Type here")
input.grid(column= 4, row= 3) 






mainWindow.mainloop()