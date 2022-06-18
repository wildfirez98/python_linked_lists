class Node: # Create a class for the Nodes. Each node will contain two fields the data and the reference link
    def __init__(self, data, reference=None): # Use __init__ method to initialize the attributes of the class. We want data and reference to be created for each node
        self.data = data # Use 'self' keyword to bind the attributes with the given arguements. Allows us to access the attributes & methods of the class in Python
        self.reference = reference


node1 = Node(5) # Create our first node
node2 = Node(11) # Create our second node

node1.reference = node2

print(node1.data) # Just prints 5 from the first node         
print(node1.reference) # Prints the memory address reference for the node

class LinkedList: # This class will store the head of the list. Initially create an empty linked list by setting head equal to none
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self): # Define a method to traverse a linked list. Will go thru and print the data of each node.
        if self.head is None: # If linked list is empty, print the below
            print("The linked list is empty")
        else: # If linked list is not empty, print each node's data & use the reference to access each node
            c_node = self.head
            while c_node is not None:
                print(c_node.data)
                c_node = c_node.reference # Reference of the node becomes the new current node equal to the reference link to go to the next node until the reference link is none
    def add_to_start(self, data): # Add a node to the begining of a linked list
        n_node = Node(data) # Set a variable that will store data from each new node created using the node class
        n_node.reference = self.head # Set the reference to the next node as the current head
        self.head = n_node # Set the current head as the new node
    

linked_list1 = LinkedList()
linked_list1.add_to_start(82)
linked_list1.add_to_start(15)
linked_list1.add_to_start(27)
linked_list1.add_to_start(49)
linked_list1.print_linked_list()