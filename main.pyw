from classes import *
from pand import generate_nodes
def main():
    # n1 = Node("Place 1")
    # n2 = Node("Place 2")
    # n3 = Node("Place 3")
    # n4 = Node("Place 4")
    # n5 = Node("Place 5")
    # n6 = Node("Place 6")
    # n7 = Node("Place 7")

    # n1.connect(n2, 2)
    # n1.connect(n3, 3)
    # n1.connect(n4, 1)

    # n2.connect(n1, 1)
    # n2.connect(n4, 5)
    # n2.connect(n6, 2)

    # n3.connect(n6, 3)
    
    # n4.connect(n5, 1)
    
    # n5.connect(n7, 1)

    # n6.connect(n7, 4)

    # print(n1.find_path(n7))

    nodes = generate_nodes()
    a: Node = nodes['Lot D']
    b: Node = nodes['Sequoia']
    print(a.find_path(b))
    
if __name__ == "__main__":
    main()