import pandas as pd
import math as m
import classes as c
import numpy as np
import json

d_f = pd.read_csv("distance.csv",usecols= [0,2],nrows =94,header = None)

def load_nodes():
    nodes = {}
    for i in range(len(d_f)):
        data_list = list(d_f.iloc[i])
        singular_string  = data_list[0]
        split_string = singular_string.split(" to ")
        name = split_string[0]
        dest_name = split_string[1]

        second_str = data_list[1]
        second_str = second_str.split(", ")
        # print(second_str)

        sec_str = second_str[1].split(" ")
        number = sec_str[0]
        unit = sec_str[1]
        
        if unit == 'ft':
            number = int(number)/5280
        #print(f'{singular_string}: {number} mi')

        
        if name not in nodes:
            nodes[name] = []
        
        nodes[name].append([dest_name, number])
        
    try:
        with open("nodes.json", "w+") as f:
            json.dump(nodes, f)
    except:
        print("Could not save nodes to json!")
        
    return nodes

def generate_nodes() -> dict:
    try:
        nodes_destinations = json.load()
    except:
        nodes_destinations = load_nodes()
    
    output_nodes = {}

    for node_map in nodes_destinations:
        node = c.Node(node_map)
        output_nodes[node_map] = node

    for node in output_nodes:
        dests = nodes_destinations[node]
        for dest in dests:
            dest_name = dest[0]
            dest_dist = dest[1]
            output_nodes[node].connect(output_nodes[dest_name], dest_dist)

    return output_nodes