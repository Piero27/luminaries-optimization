#HOMELYSM (Home Lighting System Manager)

# Creator Contact: pieroruesta2010@hotmail.com - https://github.com/Piero27
# Principal Collabority and creator of GUI: espartanlook777@gmail.com - https://github.com/jephersond

from tkinter import *
from tkinter import ttk
from algorithm import GeneticAlgorithm

# Iniatilize GUI method
root = Tk()

# Principal config of GUI
root.title("HOMELYSM")
root.iconbitmap("ICON_HOMELYSM.ico")
root.resizable(False,False)

# Font of principal labels
negrita_font = ("Helvetica", 10, "bold")

opcion = IntVar()

# Electrical System
label_select_system = Label(root,
                      text = "Select electrical system", font=negrita_font).grid(row = 0, column = 0, sticky = "w")

Radiobutton(root,
           text="American - Voltage: 110 V - Frequency: 50 Hz", 
           variable=opcion, 
           value=110).grid(row = 1, column = 0)

Radiobutton(root,
           text="Peruvian - Voltage : 220 V - Frequency : 60 Hz",
           variable=opcion, 
           value=220).grid(row = 1, column = 1)

# Square meters of room
label_select_room = Label(root, 
                    text = "Select room", font=negrita_font).grid(row = 3, column = 0, sticky="w")

label_metros_cuadrados = Label(root,text = "Square Meters:").grid(row = 4, column = 0)

metros_cuadrados = IntVar()

entry_metros_cuadrados = Entry(root)
entry_metros_cuadrados.grid(row = 4, column=1)

# Input room name and database from peruvian law
option_dict = {
    "Bedroom": 50,
    "Bathroom": 100,
    "Kitchen": 300,
    "Dining Room": 100,
    "Living Room": 100,
    "Storage Room": 500,
    "Hallways": 100,
    "Stairs": 150,
    "Game Room": 300,
    "Reading Room": 500,
    "Study": 500,
    "Indoor Parking": 50,
    "Patio": 20
}

value_inside = StringVar()

value_inside.set("Select an Option")

options_list = list(option_dict.keys())
question_menu = OptionMenu(root, value_inside, *options_list)
question_menu.grid(row = 4, column = 2)

# Luminarie 1 Data
Label(root, text = "Luminarie  1", font=negrita_font).grid(row = 6, column = 0, sticky="w")
Label(root, text = "Price ($)").grid(row = 7, column = 0)
Label(root, text = "Power (W)").grid(row= 7, column = 1)
Label(root, text = "Lumens (Lm)").grid(row= 7, column = 2)

entry_price_1 = Entry(root)
entry_price_1.grid(row = 8, column = 0, padx = 80)

entry_power_1 = Entry(root)
entry_power_1.grid(row = 8, column = 1, padx = 80)

entry_lumens_1 =Entry(root)
entry_lumens_1.grid(row = 8, column = 2, padx = 80)

# Luminarie 2 Data
Label(root, text = "Luminarie  2", font=negrita_font).grid(row = 10, column = 0, sticky="w")
Label(root, text = "Price ($)").grid(row = 11, column = 0)
Label(root, text = "Power (W)").grid(row= 11, column = 1)
Label(root, text = "Lumens (Lm)").grid(row= 11, column = 2)

entry_price_2 = Entry(root)
entry_price_2.grid(row = 12, column = 0, padx = 80)

entry_power_2 = Entry(root)
entry_power_2.grid(row = 12, column = 1, padx = 80)

entry_lumens_2 = Entry(root)
entry_lumens_2.grid(row = 12, column = 2, padx = 80)

# Luminarie 3 Data
Label(root, text = "Luminarie  3", font=negrita_font).grid(row = 14, column = 0, sticky="w")
Label(root, text = "Price ($)").grid(row = 15, column = 0)
Label(root, text = "Power (W)").grid(row= 15, column = 1)
Label(root, text = "Lumens (Lm)").grid(row= 15, column = 2)

entry_price_3 = Entry(root)
entry_price_3.grid(row = 16, column = 0, padx = 80)

entry_power_3 = Entry(root)
entry_power_3.grid(row = 16, column = 1, padx = 80)

entry_lumens_3 = Entry(root)
entry_lumens_3.grid(row = 16, column = 2, padx = 80)

# Button's function  
def clear():
    box_see.config(state=NORMAL)
    box_see.delete(1.0,END)
    box_see.config(state=DISABLED)
    
    return None

def print_results():
    box_see.config(state=NORMAL)
    box_see.insert(INSERT,"Room Chosen: %s - Area: %s\n"%(value_inside.get(), int(entry_metros_cuadrados.get())))
    box_see.config(state=DISABLED)
    
    a = int(option_dict[value_inside.get()])
    b = int(entry_metros_cuadrados.get())
    
    luminarie_1 = [float(entry_price_1.get()), float(entry_power_1.get()), float(entry_lumens_1.get())]
    
    luminarie_2 = [float(entry_price_2.get()), float(entry_power_2.get()), float(entry_lumens_2.get())]

    luminarie_3 = [float(entry_price_3.get()), float(entry_power_3.get()), float(entry_lumens_3.get())]
    
    value_calculated = GeneticAlgorithm(100,100,luminarie_1[1],luminarie_2[1],luminarie_3[1],luminarie_1[2],luminarie_2[2],luminarie_3[2],a*b)
    
    amper_calculated = (value_calculated[0]*luminarie_1[1] + value_calculated[1]*luminarie_2[1] + value_calculated[2]*luminarie_3[1])/opcion.get()
    amper_calculated = amper_calculated*1000
    
    #Output in screen
    box_see.config(state=NORMAL)
    box_see.insert(INSERT,f"{'-'*75}\n")
    box_see.insert(INSERT, f"| Luminarie{' '*32} | Number{' '*7} | Cost{' '*7} |\n")
    box_see.insert(INSERT,f"{'-'*75}\n")
    box_see.insert(INSERT, f"| Luminarie 1{' '*30} | {round(value_calculated[0],0)}{' '*(13 - len(str(value_calculated[0])))} | {value_calculated[0]*luminarie_1[0]}{' '*(11 - len(str(round(value_calculated[0]*luminarie_1[0],2))))} |\n")
    box_see.insert(INSERT,f"{'-'*75}\n")
    box_see.insert(INSERT, f"| Luminarie 2{' '*30} | {round(value_calculated[1],0)}{' '*(13 - len(str(value_calculated[1])))} | {value_calculated[1]*luminarie_2[0]}{' '*(11 - len(str(round(value_calculated[1]*luminarie_2[0],2))))} |\n")
    box_see.insert(INSERT,f"{'-'*75}\n")
    box_see.insert(INSERT, f"| Luminarie 3{' '*30} | {round(value_calculated[2],0)}{' '*(13 - len(str(value_calculated[2])))} | {value_calculated[2]*luminarie_3[0]}{' '*(11 - len(str(round(value_calculated[2]*luminarie_3[0],2))))} |\n")
    box_see.insert(INSERT,f"{'-'*75}\n")
    box_see.insert(INSERT, f"{' '*43} | Total{' '*8} | {round(value_calculated[0]*luminarie_1[0] + value_calculated[1]*luminarie_2[0] + value_calculated[2]*luminarie_3[0],3)}{' '*(11 - len(str(round(value_calculated[0]*luminarie_1[0] + value_calculated[1]*luminarie_2[0] + value_calculated[2]*luminarie_3[0],2))))} |\n ")
    box_see.insert(INSERT,f"{' '*43}{'-'*31} \n")
    box_see.insert(INSERT, f"{' '*43} | Amperage (mA) | {round(amper_calculated,2)}{' '*(11 - len(str(round(amper_calculated,2))))} |\n")
    box_see.insert(INSERT,f"{' '*44}{'-'*31} \n")
    box_see.config(state=DISABLED)
    
    return None 

# Button Clear Screen
submit_button = Button(root, text='Clear Screen', command=clear).grid(row=19,column=0)

# Output from the algorithm
box_see = Text(root, height=14, state=DISABLED)
box_see.grid(row=19,column=1, pady=10)

# Button Calculate Luminaries
calculate_button = Button(root, text="Calculate Luminaries", command=print_results).grid(row=19,column=2)

# Horizontal separator 1
separator1 = ttk.Separator(root, orient='horizontal')
separator1.grid(row=2, column=0, columnspan=3, sticky='ew', pady=10)

# Horizontal separator 2
separator2 = ttk.Separator(root, orient='horizontal')
separator2.grid(row=5, column=0, columnspan=3, sticky='ew', pady=10)

# Horizontal separator 3
separator3 = ttk.Separator(root, orient='horizontal')
separator3.grid(row=9, column=0, columnspan=3, sticky='ew', pady=10)

# Horizontal separator 4
separator4 = ttk.Separator(root, orient='horizontal')
separator4.grid(row=13, column=0, columnspan=3, sticky='ew', pady=10)

# Horizontal separator 5
separator4 = ttk.Separator(root, orient='horizontal')
separator4.grid(row=18, column=0, columnspan=3, sticky='ew', pady=10)

if __name__ == "__main__":
    root.mainloop()