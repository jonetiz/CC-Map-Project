# Gui File
import tkinter as tk
from pand import node_list

map = tk.Tk()

map.title('Columbia College Route Finder')
map.geometry('800x800')
map.configure(bg='light grey')

words1 = "Starting Location"
label1 = tk.Label(map, bg= 'white', text = words1, font = (24) , anchor = 'center')
label1.place(x= 150, y= 50, anchor = 'center')

words2 = "Ending Location"
label2 = tk.Label(map, bg= 'white', text = words2, font = (24) , anchor = 'center')
label2.place(x= 650, y= 50, anchor = 'center')

# This stuff might be unneeded
# def show():
#     drop1.configure(text= clicked.get())

# node_list is going to be changed
options = node_list

clicked = tk.StringVar()

drop1 = tk.OptionMenu(map, clicked, *options)
drop1.place(x=150, y= 100, anchor= 'center')

clicked2 = tk.StringVar()

drop2 = tk.OptionMenu(map, clicked2, *options)
drop2.place(x=650, y= 100, anchor= 'center')


map.mainloop()