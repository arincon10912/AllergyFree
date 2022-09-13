import pandas as pd

restaurant_choice = "Cane's" 
print("Hello welcome to ",restaurant_choice,". Choose from one of the following options: ")
df = pd.read_csv('canes.csv')

#printing column names
tally = 1
for col in df.columns:
    print(tally,".",col)
    tally += 1

#menu_category is a string holding a number choice
menu_category = input("") 
print("Here are your",menu_category,"options")

tally = 1
for row in df["entrees"]:
    print(tally,".",row)
    tally += 1

""" user selects more than once choice
list1 = ['1','2','3']
chosen = []
ask = (input(': '))
ask = ask.split(',')
for asks in ask:
    if asks in list1:
        chosen.append(asks)
print(chosen) """