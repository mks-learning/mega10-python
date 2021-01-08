from tkinter import *

mywindow = Tk()

def clear_entry():
    t1.delete('1.0','end')
    return


def km_to_miles():
    kilometers = float(e1_value.get())*1.62
    clear_entry()
    t1.insert(END, kilometers)


b1 = Button(mywindow, text='Convert to Kilometers', command=km_to_miles)
b1.grid(row=2, column=3)

e1_value = StringVar()
e1 = Entry(mywindow, textvariable=e1_value)
e1.grid(row=1, column=3)

t1 = Text(mywindow, heigh=1, width=20)
t1.grid(row=3, column=3)






mywindow.mainloop()
# the line about must be the last line of the program as it is the window frame that will be displayed.