# Ariadne Rincon
# File where I am practicing how to make and customize frames with tkinter
# PROJECT START
import tkinter as tk
import pandas as pd            
from tkinter import CENTER, BooleanVar, IntVar, Radiobutton, font as tkfont


#Shared details for all classes
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        self.chosen_allergens = []
        self.allergen_list = ["soy", "wheat", "nuts", "fish", "eggs"]
        self.food_list = ["Canes", "Panda Express", "Popeyes", "McDonald's", "Chick-Fil-A"]
        self.csv_list = ["canes_allergens.csv", "panda_allergies.csv", "popeyes.csv"] #need to make mcd and cfa allergen csv and include here !!
        self.boolean_list = [False, False, False, False, False]

        self.r = 0
        self.user_allergens = []

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

    # Function to change frames
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    # Function to transform boolean inputs to string of chosen allergen name
    def set_inputs(self, var1, var2, var3, var4, var5):
        self.boolean_list[0] = var1.get()
        self.boolean_list[1] = var2.get()
        self.boolean_list[2] = var3.get()
        self.boolean_list[3] = var4.get()
        self.boolean_list[4] = var5.get()

        i = 0
        for items in self.boolean_list:
            if self.boolean_list[i] is True:
                self.chosen_allergens.append(self.allergen_list[i])
            i += 1
    
    # Function to transform int value to string of restaurant name 
    def set_radio(self, var1):
        self.r = var1.get()
        print(self.food_list[(var1.get()-1)])

    # Function to display a text widget with list of safe foods 
    def return_options(self):
        input_csv = self.csv_list[(self.r-1)]
        df = pd.read_csv(input_csv)
        safe_foods = []
        T = tk.Text(self, height = 5, width = 52)

        # will print all the items that do NOT contain the allergen
        # need to work on how this will adapt when there are changing number of allergens 
        # ex. user is only allergic to "soy" VS "soy", "eggs", "wheat"
        # need to add more conditions to if statement
        index = 0
        for item in self.chosen_allergens:
            for row in df["soy"]:
                if(df.at[index, item]==0):
                    safe_foods.append([df.at[index, "product"]])
                index += 1
        T.pack()
        return T.insert(tk.END, safe_foods)

#Frame with checkboxes
class AllergyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Check all your known allergies:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        soy = BooleanVar()
        wheat = BooleanVar()
        nuts = BooleanVar()
        fish = BooleanVar()
        eggs = BooleanVar()

        c1 = tk.Checkbutton(self, text="soy", variable=soy)
        c2 = tk.Checkbutton(self, text="wheat", variable=wheat)
        c3 = tk.Checkbutton(self, text="nuts", variable=nuts)
        c4 = tk.Checkbutton(self, text="fish", variable=fish)
        c5 = tk.Checkbutton(self, text="eggs", variable=eggs)

        c1.pack()
        c2.pack()
        c3.pack()
        c4.pack()
        c5.pack()

        # must be a seperate button to call on display_input
        # will show boolean values of the checkbox choices in order 
        confirm_button = tk.Button(self, text="Confirm Choices",
                            command=lambda: controller.set_inputs(soy, wheat, nuts, fish, eggs))

        next_button = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame("FoodSelectionPage"))
        quit_button = tk.Button(self, text="Quit",command = quit)

        confirm_button.pack()
        next_button.pack()
        quit_button.pack()

#Frame with Food Options
class FoodSelectionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose a Food Option: ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        radio = IntVar()
        canes = tk.Radiobutton(self, text = "Canes", variable = radio, value = 1)
        panda = tk.Radiobutton(self, text = "Panda Express", variable = radio, value = 2)
        popeyes = tk.Radiobutton(self, text = "Popeyes", variable = radio, value = 3)
        mcd = tk.Radiobutton(self, text = "McDonald's", variable = radio, value = 4)
        cfa = tk.Radiobutton(self, text = "Chick-Fil-A", variable = radio, value = 5)

        canes.pack()
        panda.pack()
        popeyes.pack()
        mcd.pack()
        cfa.pack()

        confirm_button = tk.Button(self, text="Confirm Choices",
                            command=lambda: controller.set_radio(radio))
        next_button = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("OptionsPage"))
        quit_button = tk.Button(self, text="Quit",command = quit)

        confirm_button.pack()
        next_button.pack()
        quit_button.pack()

#Frame with Safe Food Options
class OptionsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Here are the Allergen-Free Options for You:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        # Had to make a new button in order to pause the program and allow time for the user to input their data
        # and then to use that user data and find the products that are safe for them to eat.
        # I learned that the widgets' code all runs from the beginning and does not allow for the data to be used in between
        # frames unless triggered by a button.

        display_button = tk.Button(self, text = "Show my Options", command=lambda: controller.return_options())
        back_button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("FoodSelectionPage"))
        quit_button = tk.Button(self, text="Quit",command = quit)

        display_button.pack()
        back_button.pack()
        quit_button.pack()

#Keep Program Running 
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()