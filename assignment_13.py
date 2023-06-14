# .............................ans 1.........................
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert node in a linked list
def insert(root, item):
    temp = Node(0)
    temp.data = item
    temp.next = None

    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next

        ptr.next = temp

    return root


# Function which returns new linked list
def newList(root1, root2):
    ptr1 = root1
    ptr2 = root2

    root = None
    while (ptr1 != None):
        temp = Node(0)
        temp.next = None

        # Compare for greater node
        if (ptr1.data < ptr2.data):
            temp.data = ptr2.data
        else:
            temp.data = ptr1.data

        if (root == None):
            root = temp
        else:
            ptr = root
            while (ptr.next != None):
                ptr = ptr.next

            ptr.next = temp

        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return root


def display(root):
    while (root != None):
        print(root.data, "->", end=" ")
        root = root.next

    print(" ");


# Driver Code
if __name__ == '__main__':
    root1 = None
    root2 = None
    root = None

    # First linked list
    root1 = insert(root1, 5)
    root1 = insert(root1, 2)
    root1 = insert(root1, 3)
    root1 = insert(root1, 8)

    print("First List: ", end=" ")
    display(root1)

    # Second linked list
    root2 = insert(root2, 1)
    root2 = insert(root2, 7)
    root2 = insert(root2, 4)
    root2 = insert(root2, 5)

    print("Second List: ", end=" ")
    display(root2)

    root = newList(root1, root2)
    print("New List: ", end=" ")
    display(root)



# .................................ans 2......................................

class Node:

	# Constructor to initialize
	# the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node
	# at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Given a reference to the head of a
	# list and a key, delete the first
	# occurrence of key in linked list
	def deleteNode(self, key):

		# Store head node
		temp = self.head

		# If head node itself holds the
		# key to be deleted
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		# Search for the key to be deleted,
		# keep track of the previous node as
		# we need to change 'prev.next'
		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		# if key was not present in
		# linked list
		if(temp == None):
			return

		# Unlink the node from linked list
		prev.next = temp.next

		temp = None

	# Utility function to print the
	# linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=' ')
			temp = temp.next

	# This function removes duplicates
	# from a sorted list
	def removeDuplicates(self):
		temp = self.head
		if temp is None:
			return
		while temp.next is not None:
			if temp.data == temp.next.data:
				new = temp.next.next
				temp.next = None
				temp.next = new
			else:
				temp = temp.next
		return self.head


# Driver Code
llist = LinkedList()

llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
	"duplicate elements:")
llist.removeDuplicates()
llist.printList()



# ..............................ans 3.....................................
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverse(self, head, k):

        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        # Reverse first k nodes of the linked list
        while (current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        # next is now a pointer to (k+1)th node recursively call for the list starting
        # from current. And make rest of the list as next of first node
        if next is not None:
            head.next = self.reverse(next, k)

        # prev is new head of the input list
        return prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next


# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)

print("\nReversed Linked list")
llist.printList()



# ......................................ans 4........................................
import math
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Reverses alternate k nodes and
# returns the pointer to the new head node
def kAltReverse(head, k):
    current = head
    next = None
    prev = None
    count = 0

    # 1) reverse first k nodes of the linked list
    while (current != None and count < k):
        next = current.next
        current.next = prev
        prev = current
        current = next
        count = count + 1;

    # 2) Now head pos to the kth node.
    # So change next of head to (k+1)th node
    if (head != None):
        head.next = current

    # 3) We do not want to reverse next k
    # nodes. So move the current
    # pointer to skip next k nodes
    count = 0
    while (count < k - 1 and current != None):
        current = current.next
        count = count + 1

    # 4) Recursively call for the list
    # starting from current.next. And make
    # rest of the list as next of first node
    if (current != None):
        current.next = kAltReverse(current.next, k)

    # 5) prev is new head of the input list
    return prev


# UTILITY FUNCTIONS
# Function to push a node
def push(head_ref, new_data):
    # allocate node
    new_node = Node(new_data)

    # put in the data
    # new_node.data = new_data

    # link the old list of the new node
    new_node.next = head_ref

    # move the head to po to the new node
    head_ref = new_node

    return head_ref


# Function to print linked list
def printList(node):
    count = 0
    while (node != None):
        print(node.data, end=" ")
        node = node.next
        count = count + 1


# Driver code
if __name__ == '__main__':

    # Start with the empty list
    head = None

    # create a list 1.2.3.4.5...... .20
    for i in range(20, 0, -1):
        head = push(head, i)

    print("Given linked list ")
    printList(head)
    head = kAltReverse(head, 3)

    print("\nModified Linked list")
    printList(head)




# .......................................ans 5..........................................
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to delete the last occurrence
def deleteLast(head, x):
    temp = head
    ptr = None

    while (temp != None):

        # If found key, update
        if (temp.data == x):
            ptr = temp

        temp = temp.next

    # If the last occurrence is the last node
    if (ptr != None and ptr.next == None):
        temp = head
        while (temp.next != ptr):
            temp = temp.next

        temp.next = None

    # If it is not the last node
    if (ptr != None and ptr.next != None):
        ptr.data = ptr.next.data
        temp = ptr.next
        ptr.next = ptr.next.next

    return head


# Utility function to create a new node
# with given key
def newNode(x):
    node = Node(0)
    node.data = x
    node.next = None
    return node


# This function prints contents of linked
# list starting from the given Node
def display(head):
    temp = head

    if (head == None):
        print("NULL\n")
        return

    while (temp != None):
        print(temp.data, " --> ", end="")
        temp = temp.next

    print("NULL")


# Driver code
head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(4)
head.next.next.next.next = newNode(5)
head.next.next.next.next.next = newNode(4)
head.next.next.next.next.next.next = newNode(4)

print("Created Linked list: ", end='')
display(head)

# Pass the address of the head pointer
head = deleteLast(head, 4)
print("List after deletion of 4: ", end='')

display(head)



# ...................................ans6...................................
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


# return a newnode
def newNode(key):
    return Node(key)


# driver code
# let us create two sorted linked lists to test the above
# function. Created lists shall be
# a: 5->10->15->40
# b: 2->3->20
a = Node(5)
a.next = Node(10)
a.next.next = Node(15)
a.next.next.next = Node(40)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)

v = []
while (a is not None):
    v.append(a.key)
    a = a.next

while (b is not None):
    v.append(b.key)
    b = b.next

v.sort()
result = Node(-1)
temp = result
for i in range(len(v)):
    result.next = Node(v[i])
    result = result.next

temp = temp.next
print("Resultant Merge Linked List is : ")
while (temp is not None):
    print(temp.key, end=" ")
    temp = temp.next





# .......................................ans 7...................................
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	# Constructor for empty Doubly Linked List
	def __init__(self):
		self.head = None

	# Function reverse a Doubly Linked List
	def reverse(self):
		temp = None
		current = self.head

		# Swap next and prev for all nodes of
		# doubly linked list
		while current is not None:
			temp = current.prev
			current.prev = current.next
			current.next = temp
			current = current.prev

		# Before changing head, check for the cases like
		# empty list and list with only one node
		if temp is not None:
			self.head = temp.prev

	# Given a reference to the head of a list and an
	# integer,inserts a new node on the front of list
	def push(self, new_data):

		# 1. Allocates node
		# 2. Put the data in it
		new_node = Node(new_data)

		# 3. Make next of new node as head and
		# previous as None (already None)
		new_node.next = self.head

		# 4. change prev of head node to new_node
		if self.head is not None:
			self.head.prev = new_node

		# 5. move the head to point to the new node
		self.head = new_node

	def printList(self, node):
		while(node is not None):
			print(node.data, end=' ')
			node = node.next


# Driver's code
if __name__ == "__main__":
	dll = DoublyLinkedList()
	dll.push(2)
	dll.push(4)
	dll.push(8)
	dll.push(10)

	print("\nOriginal Linked List")
	dll.printList(dll.head)

	# Function call
	dll.reverse()

	print("\nReversed Linked List")
	dll.printList(dll.head)






# ....................................ans 8...............................

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Function to delete a node in a Doubly Linked List.
# head_ref -. pointer to head node pointer.
# del -. pointer to node to be deleted.
def deleteNode(head_ref, del_):
    # base case
    if (head_ref == None or del_ == None):
        return

    # If node to be deleted is head node
    if (head_ref == del_):
        head_ref = del_.next

    # Change next only if node to be deleted is NOT
    # the last node
    if (del_.next != None):
        del_.next.prev = del_.prev

    # Change prev only if node to be deleted is NOT
    # the first node
    if (del_.prev != None):
        del_.prev.next = del_.next

    return head_ref


# Function to delete the node at the given position
# in the doubly linked list
def deleteNodeAtGivenPos(head_ref, n):
    # if list in None or invalid position is given
    if (head_ref == None or n <= 0):
        return

    current = head_ref
    i = 1

    # traverse up to the node at position 'n' from
    # the beginning
    while (current != None and i < n):
        current = current.next
        i = i + 1

    # if 'n' is greater than the number of nodes
    # in the doubly linked list
    if (current == None):
        return

    # delete the node pointed to by 'current'
    deleteNode(head_ref, current)

    return head_ref


# Function to insert a node at the beginning
# of the Doubly Linked List
def push(head_ref, new_data):
    # allocate node
    new_node = Node(0)

    # put in the data
    new_node.data = new_data

    # since we are adding at the beginning,
    # prev is always None
    new_node.prev = None

    # link the old list of the new node
    new_node.next = (head_ref)

    # change prev of head node to new node
    if ((head_ref) != None):
        (head_ref).prev = new_node

    # move the head to point to the new node
    (head_ref) = new_node

    return head_ref


# Function to print nodes in a given doubly
# linked list
def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next


# Driver program to test above functions

# Start with the empty list
head = None

# Create the doubly linked list 10<.8<.4<.2<.5
head = push(head, 5)
head = push(head, 2)
head = push(head, 4)
head = push(head, 8)
head = push(head, 10)

print("Doubly linked list before deletion:")
printList(head)

n = 2

# delete node at the given position 'n'
head = deleteNodeAtGivenPos(head, n)

print("\nDoubly linked list after deletion:")

printList(head)

