# .........................ans 1........................
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

# ................................ans 2...................................
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

	# Function to insert a new
	# node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print it
	# the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next

	def detectLoop(self):
		s = set()
		temp = self.head
		while (temp):

			# If we already have
			# this node in hashmap it
			# means there is a cycle
			# (Because we are encountering
			# the node second time).
			if (temp in s):
				return True

			# If we are seeing the node for
			# the first time, insert it in hash
			s.add(temp)

			temp = temp.next

		return False


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
	print("Loop Found")
else:
	print("No Loop ")


# ...............................ans 3.................................

class Node:
	def __init__(self, new_data):
		self.data = new_data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	# CreateNode and make linked list
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Function to get the nth node from
	# the last of a linked list
	def printNthFromLast(self, n):
		temp = self.head # Used temp variable

		length = 0
		while temp is not None:
			temp = temp.next
			length += 1

		# Print count
		if n > length: # If entered location is greater
					# than length of linked list
			print('Location is greater than the' +
				' length of LinkedList')
			return
		temp = self.head
		for i in range(0, length - n):
			temp = temp.next
		print(temp.data)


# Driver's Code
if __name__ == "__main__":
	llist = LinkedList()
	llist.push(20)
	llist.push(4)
	llist.push(15)
	llist.push(35)

	# Function call
	llist.printNthFromLast(4)


# ........................ans 4....................................

class Node:
	def __init__(self, data):

		self.data = data
		self.ptr = None

# Function to check if the linked list
# is palindrome or not


def ispalindrome(head):

	# Temp pointer
	slow = head

	# Declare a stack
	stack = []

	ispalin = True

	# Push all elements of the list
	# to the stack
	while slow != None:
		stack.append(slow.data)

		# Move ahead
		slow = slow.ptr

	# Iterate in the list again and
	# check by popping from the stack
	while head != None:

		# Get the top most element
		i = stack.pop()

		# Check if data is not
		# same as popped element
		if head.data == i:
			ispalin = True
		else:
			ispalin = False
			break

		# Move ahead
		head = head.ptr

	return ispalin

# Driver Code


# Addition of linked list
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)

# Initialize the next pointer
# of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None

# Call function to check palindrome or not
result = ispalindrome(one)

print("isPalindrome:", result)



# .........................................ans 5 ........................................
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def detectAndRemoveLoop(self):
        slow_p = fast_p = self.head

        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            # If slow_p and fast_p meet at some point then
            # there is a loop
            if slow_p == fast_p:
                self.removeLoop(slow_p)

                # Return 1 to indicate that loop is found
                return 1

        # Return 0 to indicate that there is no loop
        return 0

    # Function to remove loop
    # loop_node --> pointer to one of the loop nodes
    # head --> Pointer to the start node of the linked list
    def removeLoop(self, loop_node):
        ptr1 = loop_node
        ptr2 = loop_node

        # Count the number of nodes in loop
        k = 1
        while (ptr1.next != ptr2):
            ptr1 = ptr1.next
            k += 1

        # Fix one pointer to head
        ptr1 = self.head

        # And the other pointer to k nodes after head
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next

        # Move both pointers at the same place
        # they will meet at loop starting node
        while (ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Get pointer to the last node
        while (ptr2.next != ptr1):
            ptr2 = ptr2.next

        # Set the next node of the loop ending node
        # to fix the loop
        ptr2.next = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next


# Driver program
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop()

print("Linked List after removing loop")
llist.printList()


# .............................ans 6.................................
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def skipMdeleteN(self, M, N):
        curr = self.head

        # The main loop that traverses through the
        # whole list
        while (curr):
            # Skip M nodes
            for count in range(1, M):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                return

            # Start from next node and delete N nodes
            t = curr.next
            for count in range(1, N + 1):
                if t is None:
                    break
                t = t.next

            # Link the previous list with remaining nodes
            curr.next = t
            # Set Current pointer for next iteration
            curr = t


# Driver program to test above function

# Create following linked list
# 1->2->3->4->5->6->7->8->9->10
llist = LinkedList()
M = 2
N = 3
llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("M = %d, N = %d\nGiven Linked List is:" % (M, N))
llist.printList()
print()

llist.skipMdeleteN(M, N)

print("\nLinked list after deletion is")
llist.printList()




# ...........................ans 7...............................
class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, new_data: int):
        new_node = Node(new_data)
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node

    # Function to print linked list from the Head
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    # Main function that inserts nodes of linked list q into p at alternate positions.
    # Since head of first list never changes
    # but head of second list/ may change,
    # we need single pointer for first list and double pointer for second list.
    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head

        # swap their positions until one finishes off
        while p_curr != None and q_curr != None:
            # Save next pointers
            p_next = p_curr.next
            q_next = q_curr.next

            # make q_curr as next of p_curr
            q_curr.next = p_next  # change next pointer of q_curr
            p_curr.next = q_curr  # change next pointer of p_curr

            # update current pointers for next iteration
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr


# Driver program to test above functions
llist1 = LinkedList()
llist2 = LinkedList()

# Creating LLs

# 1.
llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)

# 2.
for i in range(8, 3, -1):
    llist2.push(i)

print("First Linked List:")
llist1.printList()

print("Second Linked List:")
llist2.printList()

# Merging the LLs
llist1.merge(p=llist1, q=llist2)

print("Modified first linked list:")
llist1.printList()

print("Modified second linked list:")
llist2.printList()



# .....................................ans 8 ...............................
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


def Circular(head):
	if head == None:
		return True

	# Next of head
	node = head.next
	i = 0

	# This loop would stop in both cases (1) If
	# Circular (2) Not circular
	while((node is not None) and (node is not head)):
		i = i + 1
		node = node.next

	return(node == head)


# Driver's code
if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	fourth = Node(4)

	llist.head.next = second
	second.next = third
	third.next = fourth

	if (Circular(llist.head)):
		print('Yes')
	else:
		print('No')

	fourth.next = llist.head

	if (Circular(llist.head)):
		print('Yes')
	else:
		print('No')

