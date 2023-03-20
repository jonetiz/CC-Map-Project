# gui File
"""
Makes a GUI for the route finder. Runs a function to determine route and travel time.
Labels and drop down boxes are used for the user to understand their starting and ending locations.
"""

# Necessary imports
import tkinter as tk
from pand import generate_nodes
from classes import Node
import datetime

map = tk.Tk()

map.title('Columbia College Route Finder')
map.geometry('800x800')
map.configure(bg = 'white')
map.resizable(False, False)

words1 = "Starting Location"
label1 = tk.Label(map, bg = 'white', text = words1, font = ('arial',24), anchor = 'center')
label1.place(x = 150, y = 50, anchor = 'center')

words2 = "Ending Location"
label2 = tk.Label(map, bg = 'white', text = words2, font = ('arial',24), anchor = 'center')
label2.place(x = 650, y = 50, anchor = 'center')

label3 = tk.Label(map, bg = 'white', text = "Speed (mph)", font=('arial', 24), anchor='center')
label3.place(x = 400, y=50, anchor='center')

slider = tk.Scale(map, bg='white', from_=1, to=10, orient='horizontal')
slider.place(x=400, y=100, anchor='center')
slider.set(3)

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
        # if this isn't the last node, add the distance (since last node connection will be extraneous)
        if i+1 < len(route):
            for n in route[i].connections:
                # if the connection is the correct node, add the conenction weight to total distance
                if n[0] is route[i+1]:
                    distance += n[1]

    print(f"{route} {distance} mi")

    # divide miles by 3 mph to get time in hours, then multiply by 3600 to get seconds.
    speed = slider.get()
    time = round((distance/speed)*3600)
    
    # format time as time delta (h:mm:ss)
    time_formatted = datetime.timedelta(seconds=time)

    distance_formatted = ""
    # if distance is more than 0.5 miles, say it in miles to 2 decimal places, else just give the number of feet.
    if distance > 0.5:
        distance_formatted = f"{round(distance, 2)} mi"
    else:
        distance_formatted = f"{round(distance*5280)} ft"

    path = ""
    for i, node in enumerate(route):
        # add node name to the path
        path += f"{node.info}"
        if i+1 is not len(route):
            # if this isn't the last node, add an arrow in between elements
            path += " -> "
            if (i+1) % 3 == 0:
                # new line for every third element
                path += "\n"
    
    # Suggested Route:
    # Node_1 -> Node_2 -> Node_3 ->
    # Node_4 -> ... -> Node_n
    # (h:mm:ss, 0.69 mi)
    results = f"Suggested Route:\n{path}\n({time_formatted} @ {speed} mph, {distance_formatted})"

    # Reconfigures a label with updated results.
    results_label.config(text = results)
    
# Button uses route function from above.
button1 = tk.Button(map, text = "Find Route", font = ('arial 24 bold'), width = 9, command = route)
button1.place(x=400, y=175, anchor ='center')

# This label is reconfigure to equal the results variable from the route function.
results_label = tk.Label(map, bg = 'white', text = "", font = ("arial", 26), anchor = 'center')
results_label.place(x = 400, y = 400, anchor = 'center')