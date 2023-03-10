import pandas as pd
import math as m
import classes as c
import numpy as np
d_f = pd.read_csv("/Users/normawallace/Desktop/magpie/distance.csv",usecols= [0,2],nrows =94,header = None)
names = []
for i in range(len(d_f)):
    # print(list(d_f.iloc[i]))
    data_list = list(d_f.iloc[i])
    singular_string  = data_list[0]
    split_string = singular_string.split(" to ")
    name = split_string[0]
    
    if name not in names:
        names.append(name)

    second_str = data_list[1]
    second_str = second_str.split(", ")
    # print(second_str)

    sec_str = second_str[1].split(" ")
    number = sec_str[0]
    unit = sec_str[1]
    
    if unit == 'ft':
        number = int(number)/5280
    print(number)

node_list = []
for i in names:
    node_list.append(c.Node(i))
print(node_list)

'''
Under Construction
'''
    

walking_speed = 3
inc = 0.1
dec = -0.1
opp = None
horiz = None
# result = m.atan(opp/horiz)
# print(result)