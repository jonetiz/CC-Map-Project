# Gui File
"""
Makes a GUI for the route finder. Runs a function to determine route and travel time.
Labels and drop down boxes are used for the user to understand their starting and ending locations.
"""

# Necessary imports
import tkinter as tk
from pand import generate_nodes
from classes import Node

map = tk.Tk()

map.title('Columbia College Route Finder')
map.geometry('800x800')
map.configure(bg = 'white')

words1 = "Starting Location"
label1 = tk.Label(map, bg = 'white', text = words1, font = ('arial',24), anchor = 'center')
label1.place(x = 150, y = 50, anchor = 'center')

words2 = "Ending Location"
label2 = tk.Label(map, bg = 'white', text = words2, font = ('arial',24), anchor = 'center')
label2.place(x = 650, y = 50, anchor = 'center')

# generate_nodes is used for the drop down menus.
options = generate_nodes()

# Manzanita and AAC were chosen as the default clicked options. This was done because of a suggestion from Joe.

clicked = tk.StringVar()
clicked.set("Manzanita")

drop1 = tk.OptionMenu(map, clicked, *options)
drop1.place(x =150, y = 100, anchor = 'center')
drop1.configure(width = 20)

clicked2 = tk.StringVar()
clicked2.set("AAC")

drop2 = tk.OptionMenu(map, clicked2, *options)
drop2.place(x = 650, y = 100, anchor = 'center')
drop2.configure(width = 20)

def route():
    """
    Finds the route and travel time and displays them in the GUI. 
    """

    # Results variable is reset to empty string at the start to stop overlap of results labels.
    results = ""
    # get start node
    start: Node = options[clicked.get()]
    # get end node
    end: Node = options[clicked2.get()]
    
    # distance variable
    distance = 0
    # the list of nodes that represent the route
    route = start.find_path(end)

    # calculate total distance of the route
    for i in range(len(route)):
        if i+1 < len(route):
            for n in route[i].connections:
                if n[0] is route[i+1]:
                    distance += n[1]

    print(route)
    print(distance)

    # Distance of route in miles is divided by 3 to find time in hours for route. 3 mph was the rate we used for walking.
    travel_time = str(distance/3)
    distance = str(distance)

    # Results variable is a string with the list specific characters removed and other strings added in.
    # I added new lines to try and make it a little interesting to look at.
    results = str(route)
    results = results.replace('<','')
    results = results.replace('>','')
    results = results.replace('[','')
    results = results.replace(']','')
    results = results.replace(',', '\nto\n')
    results = "Go from:\n" + results + "\n\nTotal Distance = " + distance + " Miles" + "\nTravel Time = " + travel_time + " Hours"

    # Reconfigures a label with updated results.
    results_label.config(text = results)
    
# Button uses route function from above.
button1 = tk.Button(map, text = "Find Route", font = ('arial 24 bold'), width = 9, command = route)
button1.place(x=400, y=100, anchor ='center')

# This label is reconfigure to equal the results variable from the route function.
results_label = tk.Label(map, bg = 'white', text = "", font = ("arial", 26), anchor = 'center')
results_label.place(x = 400, y = 400, anchor = 'center')

map.mainloop()