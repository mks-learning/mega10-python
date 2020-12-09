import from tkinter *

# Create a Python program that expects a kilogram input value and converts
#  that value to grams, pounds, and ounces when the user pushes the Convert button.   

conwindow=Tk(screenName="Conversion Tool")

# these function is what will be executed when the button in the UI is pressed. The input will be
# converted from the input of Kg to an output of g, lbs, ozs
def convert_input():
    con_grams = float(input_value) * 1000
    # 1000 grams in a kilogram
    tg.insert(END,con_grams)
    
    con_pounds = float(input_value) * 2.20462
    # 2.20462 pounds in a kg
    tp.insert(END,con_pounds)

    con_ounces = float(input_value) * 2.20462 * 16
    # 16 oz per pound and 2.20462 pounds per kg
    tpo.insert(END,con_ounces)


# below is definging a button and then the command statement is stating "when pressed execute
#  this function" (which needs to have been defined in the lines prior to this button instantiation)
kg-button = Button(conwindow, text = "Enter KGs for conversion", command=convert_input)
kg-button.grid(row=2, column=0)

input_value=StringVar()
input_value=Entry(conwindow, textvariable=input_value)
input_value.grid(row=1, column=0)

tg=Text(conwindow, height=1, width=26)
tg.grid(row=0, column=1)

tp=Text(conwindow, height=1, width=26)
tp.grid(row=1, column=1)

tpo=Text(conwindow, height=1, width=26)
tpo.grid(row=2, column=1)

conwindow.mainloop()
