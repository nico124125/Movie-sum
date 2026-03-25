from tkinter import *
import tkinter as tk
from tkinter import ttk

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# function --> on change dropdown value
# put with other functions, not with GUI code
def change_dropdown(*args):
    selection = tkvar.get()
    print('The current selection is %s.' % selection)
    print(selection)
    if selection == "Commando":
        print("You have selected %s." % selection)
        label2.configure(text="COMMANDO\n\nRetired Special Forces Colonel John Matrix is living a quiet, secluded life in the mountains with his young daughter, Jenny. His peaceful retirement is shattered\n when his former team members are murdered one by one, and a group of mercenaries led by his ex-subordinate, Bennett, kidnaps Jenny. The kidnappers\n are working for a deposed South American dictator named Arius. They give Matrix an ultimatum: fly to the country of Val Verde and assassinate the current\n president, or they will kill his daughter. Matrix has no intention of following orders. He escapes the plane just as it’s taking off and realizes he has exactly 11 hours\n until the flight lands in Val Verde (when the villains will realize he’s gone) to find where Jenny is being held. While escaping from the airport, Matrix gets into a brutal struggle\n with the henchman assigned to shadow him and ensure he boards the plane. Realizing the kidnapper’s Intel is his only lead to his daughter, Matrix kills the man during\n a high-speed car chase. During this same chase, he commandeers a vehicle driven by Cindy, an off-duty flight attendant. When Matrix explains his desperate situation,\n Cindy is understandably skeptical and attempts to alert the authorities, forcing Matrix to take charge. The movie culminates in a massive, legendary assault on a private island.\n Matrix takes on an entire private army by himself before facing off in a final, personal showdown against Bennett...", font=("Arial", 9, "bold"))
        label4.configure(text="Release Date: October 4th 1985\n Director: Mark L. Lester\n Producer: Joel Silver\n Writer: Steven E. de Souza\n Runtime: 90 minutes\n Budget: Approx. $9–10 million\n Box Office: Approx. $57.5 million worldwide\n\n                              Main Cast\nActor                                         Role\nArnold Schwarzenegger    Col. John Matrix\nRae Dawn Chong                 Cindy\nAlyssa Milano                        Jenny Matrix\nVernon Wells                         Bennett\nDan Hedaya                           Arius\nDavid Patrick Kelly              Sully\nBill Duke                                 Cooke", font=("Arial", 12, "bold"))
    if selection == "The Terminator":
        print("You have selected %s." % selection)
        label2.configure(text="The Terminator selected!")
        label4.configure(text="The Terminator selected!", font=("Arial", 12, "bold"))
    if selection == "Back to the Future":
        print("You have selected %s." % selection)
        label2.configure(text="BTTF")
        label4.configure(text="BTTF selected!", font=("Arial", 12, "bold"))
    if selection == "The 6th Day":
        print("You have selected %s." % selection)
        label2.configure(text="6th Day")
        label4.configure(text="6th Day selected!", font=("Arial", 12, "bold"))
    if selection == "Minority Report":
        print("You have selected %s." % selection)
        label2.configure(text="Minority Report")
        label4.configure(text="Minority Report selected!", font=("Arial", 12, "bold"))
        # do other 'stuff' here
    # add more here

###############################################################
# -----------The drop down menu code is above this -------------

# functions
def button_pressed():
    print("button pressed on main")
    output_label.configure(text=f"Hi  how are you?")

# --------------- Build the GUI -----------------#
window = tk.Tk()
window.title("Movie Summerizer")

# add the Notebook widget for tab control
tabControl = ttk.Notebook(window)

# add tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

# add tabls to the Notebook widget for tab control
tabControl.add(tab1, text='Movies')
tabControl.add(tab2, text='Summary')
tabControl.add(tab3, text='Info')
tabControl.pack(expand=1, fill="both")

####################################################

# ------------- Widgets on the tabs ---------------#

# on tab1
label1 = ttk.Label(tab1, text="Placeholder222")
label1.grid(column=0, row=0, padx=30, pady=30)
# Add a grid
mainframe = Frame(tab1)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# label above dropdown menu
label = Label(mainframe, text="Movie Select")
label.grid(row=0, column=1)

###############################################################
# -------------The drop down menu code is below ---------------

label2 = ttk.Label(tab2, text="Select Option From Summarizer")
label4 = ttk.Label(tab3, text="Select movie for info")
# Create a Tkinter variable
tkvar = StringVar(mainframe)
tkvar.set('Options')  # set the default option
# link function to change dropdown
tkvar.trace('w', change_dropdown)

# list with options
choices = ['The Terminator', 'Back to the Future',
           'Commando', 'The 6th Day',
           'Minority Report']

optionmenu = OptionMenu(mainframe, tkvar, *choices)
optionmenu.config(width=30)
optionmenu.grid(row=1, column=1)

# on tab2
label2.grid(column=0, row=0, padx=30, pady=30)

# on tab3
label4.grid(column=0, row=0, padx=30, pady=30)

# on tab3
label3 = ttk.Label(tab4, text="Place hold").grid(column=0, row=0, padx=30, pady=30)

window.mainloop()
