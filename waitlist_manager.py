# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None

class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self,name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self,name):
        if not self.head:
            print(f'{name} not found')
            return
        if self.head.name == name:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next


    def print_list(self,name):
        current = self.head
        if not current:
            print("The list is empty!")
        else:
            print("Waitlist:")
            while current:
                print(f'{current.name}')
                current = current.next


def waitlist_generator():
    # Create a new linked list instance
    
    list = LinkedList()
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            list.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            list.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            list.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            list.print_list(name)

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()
'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?

The list I created using node, creating an empty list that contains the init 
function to store self and name variables and the next pointer to maintain an 
empty portion of the linked list. This is possible because linked lists do not 
require each element to be accessed by its location. Throughout the linked list 
there are 5 functions that play different roles into manipulating the list. 
add_front will add a name to the top of the list, add_end will add a name to the 
end of the list, remove will remove a name (if spelled accurately) and if it is 
not in the list will let the user know that the name is not found. Print list will 
print the entire list starting with the head, unless the list is empty, then it 
will tell you it is empty! The linked list is then put into the waitlist generator 
function that uses elif statements to navigate the choices, whether that be adding
a name, removing a name, printing the list, and exiting the list and informing 
the user that they chose an invalid option in terms of editing the list in 
correspondence to its integer. The role of the head is to access each node and 
other traversing of the nodes enabling removal or addition at the beginning or 
end of the list. Linked lists can provide engineers with a foundation for data 
structures that are simple to manipulate including the way it stores memory.
'''
