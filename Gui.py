# Gui File
import tkinter as tk
from pand import generate_nodes
from classes import Node

map = tk.Tk()

map.title('Columbia College Route Finder')
map.geometry('800x800')
map.configure(bg='light grey')

words1 = "Starting Location"
label1 = tk.Label(map, bg= 'white', text = words1, font = (24), anchor = 'center')
label1.place(x= 150, y= 50, anchor = 'center')

words2 = "Ending Location"
label2 = tk.Label(map, bg= 'white', text = words2, font = (24), anchor = 'center')
label2.place(x= 650, y= 50, anchor = 'center')

words3 = "Find Route"
label3 = tk.Label(map,bg= 'white', text = words3, font= (24), anchor = 'center')
label3.place(x= 400, y= 50, anchor = 'center')

options = generate_nodes()

clicked = tk.StringVar()

drop1 = tk.OptionMenu(map, clicked, *options)
drop1.place(x=150, y= 100, anchor= 'center')

clicked2 = tk.StringVar()

drop2 = tk.OptionMenu(map, clicked2, *options)
drop2.place(x=650, y= 100, anchor= 'center')

def route():
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

button1 = tk.Button(map, width= 10, command= route)
button1.place(x=400, y=100, anchor ='center')

map.mainloop()