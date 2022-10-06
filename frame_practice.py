# Ariadne Rincon
# File where I am practicing how to make and customize frames with tkinter
# PROJECT START
import tkinter as tk    
import pandas as pd            
from tkinter import font as tkfont

#Shared details for all classes
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (AllergyPage, FoodSelectionPage, OptionsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AllergyPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#Frame with checkboxes
class AllergyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Check all your known allergies:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        #s = tk.IntVar() this may work to save variable?
        soy = tk.Checkbutton(self, text="soy")
        wheat = tk.Checkbutton(self, text="wheat")
        nuts = tk.Checkbutton(self, text="nuts")
        fish = tk.Checkbutton(self, text="fish")
        eggs = tk.Checkbutton(self, text="eggs")

        soy.pack()
        wheat.pack()
        nuts.pack()
        fish.pack()
        eggs.pack()

        confirm_button = tk.Button(self, text="Confirm Choices",
                            command=lambda: controller.show_frame("FoodSelectionPage"))
        quit_button = tk.Button(self, text="Quit",command = quit)

        confirm_button.pack()
        quit_button.pack()

#Frame with Food Options
class FoodSelectionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose a Food Option: ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        canes = tk.Radiobutton(self, text = "Canes", value = 1)
        panda = tk.Radiobutton(self, text = "Panda Express", value = 2)
        popeyes = tk.Radiobutton(self, text = "Popeyes", value = 3)
        mcd = tk.Radiobutton(self, text = "McDonald's", value = 4)
        cfa = tk.Radiobutton(self, text = "Chick-Fil-A", value = 5)

        canes.pack()
        panda.pack()
        popeyes.pack()
        mcd.pack()
        cfa.pack()

        next_button = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("OptionsPage"))
        quit_button = tk.Button(self, text="Quit",command = quit)

        next_button.pack()
        quit_button.pack()

#Frame with Safe Food Options
class OptionsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Here are the Allergen-Free Options for You:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        T = tk.Text(self, height = 5, width = 52)
        df = pd.read_csv('canes_allergies.csv')
        safe_foods = []
        index = 0
        for row in df["eggs"]:
            if(df.at[index,"eggs"] == 0):
                safe_foods.append(df.at[index, "product"])
            index += 1

        back_button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("FoodSelectionPage"))
        quit_button = tk.Button(self, text="Quit",command = quit)

        T.pack()
        back_button.pack()
        quit_button.pack()

        T.insert(tk.END, safe_foods)

#Keep Program Running 
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()