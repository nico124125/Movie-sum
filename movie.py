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
        label2.configure(text="COMMANDO\n\nRetired Special Forces Colonel John Matrix is living a quiet, secluded life in the mountains with his young daughter, Jenny. His peaceful retirement is shattered\n when his former team members are murdered one by one, and a group of mercenaries led by his ex-subordinate, Bennett, kidnaps Jenny. The kidnappers\n are working for a deposed South American dictator named Arius. They give Matrix an ultimatum: fly to the country of Val Verde and assassinate the current\n president, or they will kill his daughter. Matrix has no intention of following orders. He escapes the plane just as it’s taking off and realizes he has exactly 11 hours\n until the flight lands in Val Verde (when the villains will realize he’s gone) to find where Jenny is being held. While escaping from the airport, Matrix gets into a brutal struggle\n with the henchman assigned to shadow him and ensure he boards the plane. Realizing the kidnapper’s Intel is his only lead to his daughter, Matrix kills the man during\n a high-speed car chase. During this same chase, he commandeers a vehicle driven by Cindy, an off-duty flight attendant. When Matrix explains his desperate situation,\n Cindy is understandably skeptical and attempts to alert the authorities, forcing Matrix to take charge. The movie culminates in a massive, legendary assault on a private island.\n Matrix takes on an entire private army by himself before facing off in a final, personal showdown against Bennett...", font=("Arial", 9, "bold"))
        label4.configure(text="Release Date: October 4th 1985\n Director: Mark L. Lester\n Producer: Joel Silver\n Writer: Steven E. de Souza\n Runtime: 90 minutes\n Budget: Approx. $9–10 million\n Box Office: Approx. $57.5 million worldwide\n\n                              Main Cast\nActor                                         Role\nArnold Schwarzenegger    Col. John Matrix\nRae Dawn Chong                 Cindy\nAlyssa Milano                        Jenny Matrix\nVernon Wells                         Bennett\nDan Hedaya                           Arius\nDavid Patrick Kelly              Sully\nBill Duke                                 Cooke", font=("Arial", 12, "bold"))
    if selection == "Terminator 2":
        print("You have selected %s." % selection)
        label2.configure(text="TERMINATOR 2\n\nIn 1984, Sarah Connor, a waitress at a diner in LA, survived a lethal hunt by a T-800 Terminator sent from 2029 to prevent John connor, the future Resistance leader, from being born.\nEleven years later, a more advanced liquid-metal T-1000 is sent by Skynet to Los Angeles to assassinate her ten-year-old son, John Connor.\nIn a twist of fate, the Resistance sends back its own protector: a reprogrammed T-800, identical to the machine that once tried to kill Sarah.\nAfter John and the T-800 break a traumatized Sarah out of Pescadero State Hospital, she must overcome her terror of the machine to save the world.\nThe trio learns that Skynet's future existence is based on the salvaged arm and CPU of the first Terminator, currently being studied by Miles Dyson.\nTo prevent Judgment Day — the 1997 nuclear holocaust—they launch a raid on Cyberdyne Systems to destroy all traces of the future technology.\nThis leads to a relentless pursuit by the T-1000, culminating in a brutal, final confrontation amidst the molten vats of a massive steel mill.\nWith the T-1000 defeated, the T-800 makes the ultimate sacrifice by being lowered into the steel, ensuring no future tech remains to start the war..", font=("Arial", 9, "bold"))
        label4.configure(text="Release Date: July 3rd 1991\n Director: James Cameron\n Producer: James Cameron\n Writer: James Cameron and William Wisher Jr.\n Runtime: 137 minutes\n Budget: Approx. $94–102 million\n Box Office: $520.9 million (The highest-grossing film of 1991)\n\n                              Main Cast\nActor                                         Role\nArnold Schwarzenegger     Rebel T-800\nLinda Hamilton                      Sarah Connor\nEdward Furlong                    John Connor\nRobert Patrick                       T-1000\nJoe Morton                             Miles Dyson\nEarl Boen                                Dr. Peter Silberman", font=("Arial", 12, "bold"))
    if selection == "Back to the Future":
        print("You have selected %s." % selection)
        label2.configure(text="BACK TO THE FUTURE\n\nThe saga begins in 1985 with Marty McFly, a teenager whose life is defined by his family's mediocrity and\n his friendship with the disgraced physicist Dr. Emmett Brown. Doc transforms a DeLorean DMC-12\n into a time machine powered by a plutonium-fueled nuclear reactor, requiring a speed of 88 mph and\n 1.21 gigawatts of electricity to jump. After a botched deal with Libyan terrorists leaves Doc dead,\n Marty accidentally hits 88 mph and is transported back to 1955, where he meets his teenage parents,\n George and Lorraine. Marty inadvertently interferes with their first meeting, causing Lorraine to fall\n for him instead of George, which starts a temporal paradox that begins erasing Marty from existence.\n Stranded in 1955 without plutonium, Marty seeks out a younger Doc Brown, who is skeptical until Marty\n reveals Doc's secret 'vision' of the Flux Capacitor from earlier that day. They orchestrate a plan to\n harness a lightning strike at the Hill Valley Clock Tower to power the DeLorean, while Marty successfully\n coaches George into standing up to the bully Biff Tannen. Marty returns to a vastly improved 1985 only\n for Doc to reappear from the future, insisting they travel to 2015 to prevent Marty's son from joining\n a gang and ruining the family legacy. In 2015, while Marty is busy fixing the future, an elderly Biff\n Tannen steals the DeLorean and travels back to 1955 to give his younger self a Sports Almanac\n containing 50 years of scores. This creates a nightmarish '1985-A,' a dystopian timeline where Biff is\n a corrupt billionaire who murdered George McFly and forced Lorraine into a miserable, abusive marriage.\n Doc and Marty must return to 1955 to steal the Almanac back, meticulously avoiding their 'past selves' \n from the first movie to prevent a universe-destroying paradox during the Enchantment Under the Sea\n dance. Just as they succeed and burn the book, the DeLorean is struck by lightning while hovering,\n accidentally sending Doc Brown back to the year 1885 and leaving Marty once again in 1955.\n Marty, left stranded on a rainy road in the middle of hill vally\'s farm fields then spots car in the distance.\n a man disembarks from the car; a post man who hands marty a letter from Doc, written 70 years prior, explaining that he is living a happy\n life as a blacksmith but has hidden the DeLorean in a mine for Marty to find and go home. Upon\n discovering a gravestone revealing Doc was murdered by Buford \"Mad Dog\" Tannen just days after\n writing the letter, Marty ignores Doc's warnings and travels to 1885 to save his friend. In the Old\n West, the duo faces a critical problem: the DeLorean's fuel line is severed, and since gasoline doesn't\n exist in a non-volatile refined state yet, they cannot reach 88 mph to activate the time circuits. They hijack a steam locomotive\n to push the DeLorean down a steep, unfinished bridge, while Doc complicates the plan by falling in\n love with a schoolteacher named Clara Clayton. The climax involves a high-speed train heist where\n Doc chooses to stay in 1885 to save Clara from falling off the train, while Marty is successfully\n propelled back to a restored 1985. The DeLorean is instantly obliterated by a modern freight train\n upon arrival, but Doc eventually returns in a new time-traveling steam engine with Clara and their\n sons, Jules and Verne. The trilogy concludes with Marty learning that the future is not yet written,\n as he avoids a car accident that would have ruined his music career, finally taking control of his own destiny.", font=("Arial", 9, "bold"))
        label4.configure(text="Release Date: July 3rd 1985\nDirector: Robert Zemeckis\nProducers: Bob Gale and Neil Canton \nWriters: Robert Zemeckis and Bob Gale\nRuntime: 116 minutes\nBudget: $19,000,000\nBox Office: Approximately $381–$398 million worldwide (the highest-grossing film of 1985)\n\n                       Main Cast:\nMichael J. Fox             Marty McFly\nChristopher Lloyd     Dr. Emmett 'Doc' Brown\nLea Thompson           Lorraine Baines-McFly\nCrispin Glover            George McFly\nThomas F. Wilson      Biff Tannen", font=("Arial", 12, "bold"))
    if selection == "The 6th Day":
        print("You have selected %s." % selection)
        label2.configure(text="THE 6TH DAY\n\nIn the near future, cloning technology has advanced to the point where any pet can be 're-pet'\n for a fee, but cloning humans is strictly illegal under '6th Day' laws, named after the biblical day\n God created man. Adam Gibson, a traditionalist helicopter pilot, runs a charter business with his\n partner Hank. On Adam's birthday, they are hired to fly billionaire Michael Drucker, the CEO of the\n world's largest cloning corporation, 'Replacement Technologies'. Due to a scheduling swap, Hank\n takes the flight while Adam stays behind to celebrate. During the trip, an anti-cloning extremist\n named Tripp assassinates both Drucker and the pilot. To protect his empire and hide his death,\n Drucker—who has been illegally cloning himself for years to achieve immortality—orders his team\n to clone both himself and the pilot immediately. However, a clerical error leads the team to clone\n Adam Gibson, believing he was the one who died in the crash. When the real Adam returns home that\n night, he is horrified to see a clone of himself inside his house, celebrating with his wife and\n daughter. Before he can process the shock, Drucker's security team arrives to 'erase' him, as his\n existence is living evidence of their illegal activities. Adam is forced into a high-stakes game of\n survival, eventually discovering a vast conspiracy where the elite use 'Syncing' (uploading memories\n via cerebral snapshots) to live forever. In a major plot twist, it is revealed that the 'Adam' the\n audience has been following for most of the film is actually the clone, while the 'original' Adam\n has been working from the shadows to infiltrate Drucker's facility. The two Adams eventually team\n up, realizing that regardless of who was born and who was made, they both share the same soul and\n love for their family. They launch a final assault on 'Replacement Technologies', destroying the\n cloning vats and killing Drucker, who dies permanently when his newest, incomplete clone fails to\n stabilize. In the aftermath, the original Adam helps his clone escape to Argentina to start a new\n life in secret, while he returns to his family, finally accepting that technology doesn't define humanity.\n", font=("Arial", 9, "bold"))
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
window.title("Movie Summarizer")

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
choices = ['Terminator 2', 'Back to the Future',
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
