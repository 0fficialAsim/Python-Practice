from tkinter import *
#Widgets = Label, Button, Entry Textbox, Spinbox, Scale, Checkbox, Radiobutton, Listbox
window = Tk()
window.title("Adeola's First GUI Program")

window.minsize(width=500, height=500)

#Label 
label = Label(text="This is a label", font=("Arial", 24, "bold"))
label.pack()
#Pack places the label on the window (tkinter.Tk())

#To change the the attributes of a widiget, refer to it as a dictionary 
label["text"] = "New Text" 
#or use the config method 
label.config(text="new txt")



#Button, a diff type of widget 
def button_clicked():
    print("clicked")    
    usr_input = input.get()
    label.config(text=usr_input)
button = Button(text="Click me", font=("Arial", 16, "bold"), command=button_clicked)
button.pack()


#Entry 
input = Entry()
input.pack()
input.config(width=10)


#More Widets 

#Text
textBox = Text(height=5,width=20,font=("Arial", 16, "bold"))
textBox.pack()



#Tkinker Layout Managers 
"""
Pack(), Place(), Grid() 

Place() - Meant for prescise positioning 
Grid() - Allows for grid placing, define column and row in method

#Cannot use grid and pack simtaneoulsy! 
"""

new_label = Label(text="New Label", font=("Arial", 24))
new_label.place(x=0,y=0)

new_label.grid(column=2, row=2)











window.mainloop()
