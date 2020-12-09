from tkinter import *
 
 
def kg_converter():
    clear_texts()  # to stop appending
    data = float(e1_value.get())
    grams = data*1000
    pounds = data*2.20462
    ounces = data*35.274
 
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)
 
 
def clear_texts():
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)
 
 
window = Tk()
 
# labels
l1 = Label(window, text="Kg")
l2 = Label(window, text="gm")
l3 = Label(window, text="lb")
l4 = Label(window, text="oz")
 
# buttons
b1 = Button(window, text="Convert", command=kg_converter)
 
# entries
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
 
# textboxes
t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)
 
 
# grid layout
# 0:6
l1.grid(row=0, column=0, columnspan=2)
e1.grid(row=0, column=3)
b1.grid(row=0, column=4, columnspan=2)
# 1:6
t1.grid(row=1, column=1)
l2.grid(row=1, column=2)
t2.grid(row=1, column=3)
l3.grid(row=1, column=4)
t3.grid(row=1, column=5)
l4.grid(row=1, column=6)
 
 
window.mainloop()