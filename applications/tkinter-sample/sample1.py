from tkinter import *
# best practice is to import all functions from tkinter (*) instead of one at a time

# use Tk() function to create the window of the UI (for on prem applications) and use Tk() to 
mywindow = Tk()

# this function is what will be executed when the button in the UI is pressed. The input will be
# converted from the input of KM to an output of MI
def miles_to_km():
#    miles = k * 1.62
#   return miles
# since e1_value is defined as a StringVar() (rem this is a function statement) you need to use
# get() to signify get the value of the string variable e1_value.
    km = float(e1_value.get()) * 1.62
    t1.insert(END, km)

# below is definging a button and then the command statement is stating "when pressed execute
#  this function" (which needs to have been defined in the lines prior to this button instantiation)
b1 = Button(mywindow, text = "Enter Miles to get Kilometers", command=miles_to_km)
b1.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(mywindow, textvariable=e1_value)
e1.grid(row=0, column=1)

t1=Text(mywindow, height=1, width=26)
t1.grid(row=1, column=1)

mywindow.mainloop()
