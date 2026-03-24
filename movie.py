
from tkinter import *
import tkinter as tk
from tkinter import ttk

# function --> on change dropdown value
# put with other functions, not with GUI code
def change_dropdown(*args):
    selection = tkvar.get()
    print('The current selection is %s.' % selection)
    print(selection)
    if selection == "Commando":
        print("You have selected %s." % selection)
        label2.configure(text="Test")
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
label1 = ttk.Label(tab1, text="Welcome to \
		GeeksForGeeks").grid(column=0, row=0, padx=30, pady=30)
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
label2 = (ttk.Label(tab2, text="Placehold"))
label2.grid(column=0, row=0, padx=30, pady=30)


# on tab3
label4 = ttk.Label(tab2, text="Placehold").grid(column=0, row=0, padx=30, pady=30)

# on tab3
label3 = ttk.Label(tab3, text="Place hold").grid(column=0, row=0, padx=30, pady=30)



window.mainloop()
