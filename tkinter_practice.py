#Pop up window
"""import tkinter as tk

root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Hi Ximena")
message.pack()

# keep the window displaying
root.mainloop()"""

#One checkbox
"""import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('200x200')
root.resizable(False, False)
root.title('Checkbox Demo')

allergens = tk.StringVar()


def allergens_changed():
    tk.messagebox.showinfo(title='My Allergies:',
                        message=allergens.get())


ttk.Checkbutton(root,
                text='Soy',
                command=allergens_changed,
                variable=allergens,
                onvalue='agree',
                offvalue='disagree').pack()


root.mainloop()"""

#project start
import pandas as pd
from tkinter import *
from tkinter import messagebox
import tkinter

master = tkinter.Tk()

def var_states():
   print("Your Allergies: soy: %d wheat: %d nuts: %d fish: %d eggs: %d" % 
        (var1.get(),  var2.get(), var3.get(), var4.get(), var5.get()))

def open_window():
    messagebox.showinfo(title = "Your Allergies", message = var_states())

Label(master, text="Check all your known allergies:").grid(row=0, sticky=W)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

Checkbutton(master, text="soy", variable=var1).grid(row=1, sticky=W)
Checkbutton(master, text="wheat", variable=var2).grid(row=2, sticky=W)
Checkbutton(master, text="nuts", variable=var3).grid(row=3, sticky=W)
Checkbutton(master, text="fish", variable=var4).grid(row=4, sticky=W)
Checkbutton(master, text="eggs", variable=var5).grid(row=5, sticky=W)

Button(master, text='Next', command=open_window).grid(row=6, sticky=W, pady=4)
Button(master, text='Quit', command=quit).grid(row=7, sticky=W, pady=4)


mainloop()

restaurant_choice = "Cane's" 
#print("Hello welcome to ",restaurant_choice,". Choose from one of the following options: ")
df = pd.read_csv('canes_allergies.csv')

#printing column names
"""tally = 1
for col in df.columns:
    print(tally,".",col)
    tally += 1"""

#menu_category is a string holding a number choice
#menu_category = input("") 
print("Here are your options: ")

for row in df["soy"]:
    print(row)


#Possibly to display table on tkinter
"""rows = []
for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=GROOVE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)"""