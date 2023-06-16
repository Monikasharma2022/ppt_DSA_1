# .......................................ans 1....................................
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




# ..........................................ans 2.........................................
import sys
import math

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Function to create a new node with given data */


def newNode(data):
	return Node(data)

# Function to reverse the linked list */


def reverseList(head):
	if not head:
		return
	curNode = head
	prevNode = head
	nextNode = head.next
	curNode.next = None

	while(nextNode):
		curNode = nextNode
		nextNode = nextNode.next
		curNode.next = prevNode
		prevNode = curNode

	return curNode

# Adds one to a linked lists and return the head
# node of resultant list


def addOne(head):

	# Reverse linked list and add one to head
	head = reverseList(head)
	k = head
	carry = 0
	prev = None
	head.data += 1

	# update carry for next calculation
	while(head != None) and (head.data > 9 or carry > 0):
		prev = head
		head.data += carry
		carry = head.data // 10
		head.data = head.data % 10
		head = head.next

	if carry > 0:
		prev.next = Node(carry)
	# Reverse the modified list
	return reverseList(k)

# A utility function to print a linked list


def printList(head):
	if not head:
		return
	while(head):
		print("{}".format(head.data), end="")
		head = head.next


# Driver code
if __name__ == '__main__':
	head = newNode(1)
	head.next = newNode(9)
	head.next.next = newNode(9)
	head.next.next.next = newNode(9)

	print("List is: ", end="")
	printList(head)

	head = addOne(head)

	print("\nResultant list is: ", end="")
	printList(head)





# ....................................ans 3.................................
class Node():
	def __init__(self, data):
		self.data = data
		self.right = None
		self.down = None


class LinkedList():
	def __init__(self):

		# head of list
		self.head = None

	# Utility function to insert a node at beginning of the
	# linked list
	def push(self, head_ref, data):

		# 1 & 2: Allocate the Node &
		# Put in the data
		new_node = Node(data)

		# Make next of new Node as head
		new_node.down = head_ref

		# 4. Move the head to point to new Node
		head_ref = new_node

		# 5. return to link it back
		return head_ref

	def printList(self):

		temp = self.head
		while(temp != None):
			print(temp.data, end=" ")
			temp = temp.down

		print()

	# An utility function to merge two sorted linked lists
	def merge(self, a, b):
		# if first linked list is empty then second
		# is the answer
		if(a == None):
			return b

		# if second linked list is empty then first
		# is the result
		if(b == None):
			return a

		# compare the data members of the two linked lists
		# and put the larger one in the result
		result = None

		if (a.data < b.data):
			result = a
			result.down = self.merge(a.down, b)
		else:
			result = b
			result.down = self.merge(a, b.down)

		result.right = None
		return result

	def flatten(self, root):

		# Base Case
		if(root == None or root.right == None):
			return root
		# recur for list on right

		root.right = self.flatten(root.right)

		# now merge
		root = self.merge(root, root.right)

		# return the root
		# it will be in turn merged with its left
		return root


# Driver's code
if __name__ == '__main__':
	L = LinkedList()

	'''
	Let us create the following linked list
			5 -> 10 -> 19 -> 28
			| |	 |	 |
			V V	 V	 V
			7 20 22 35
			|		 |	 |
			V		 V	 V
			8		 50 40
			|			 |
			V			 V
			30			 45
	'''
	L.head = L.push(L.head, 30)
	L.head = L.push(L.head, 8)
	L.head = L.push(L.head, 7)
	L.head = L.push(L.head, 5)

	L.head.right = L.push(L.head.right, 20)
	L.head.right = L.push(L.head.right, 10)

	L.head.right.right = L.push(L.head.right.right, 50)
	L.head.right.right = L.push(L.head.right.right, 22)
	L.head.right.right = L.push(L.head.right.right, 19)

	L.head.right.right.right = L.push(L.head.right.right.right, 45)
	L.head.right.right.right = L.push(L.head.right.right.right, 40)
	L.head.right.right.right = L.push(L.head.right.right.right, 35)
	L.head.right.right.right = L.push(L.head.right.right.right, 20)

	# Function call
	L.head = L.flatten(L.head)

	L.printList()





# ........................................ans 4...................................
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.arbit = None

# Function to clone the linked list
def cloneLinkedList(head):
	# Map to store the mapping of
	# old nodes with new ones
	mp = {}
	temp = head
	nhead = Node(temp.val)
	mp[temp] = nhead

	# Loop to create duplicates of nodes
	# with only next pointer
	while temp.next:
		nhead.next = Node(temp.next.val)
		temp = temp.next
		nhead = nhead.next
		mp[temp] = nhead

	temp = head

	# Loop to clone the arbit pointers
	while temp:
		mp[temp].arbit = mp[temp.arbit]
		temp = temp.next

	# Return the head of the clone
	return mp[head]

# Function to print the linked list
def printList(head):
	result = []
	while head:
		result.append(f"{head.val}({head.arbit.val})")
		head = head.next
	print(" -> ".join(result))

# Creating a linked list with random pointer
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.arbit = head.next.next
head.next.arbit = head
head.next.next.arbit = head.next.next.next.next
head.next.next.next.arbit = head.next.next
head.next.next.next.next.arbit = head.next

# Print the original list
print("The original linked list:")
printList(head)

# Function call
sol = cloneLinkedList(head)

print("The cloned linked list:")
printList(sol)




# ...............................ans 5........................................
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # A utility function to create
    # a new node
    def newNode(self, key):
        temp = Node(key)
        self.next = None
        return temp

    # Rearranges given linked list
    # such that all even positioned
    # nodes are before odd positioned.
    # Returns new head of linked List.
    def rearrangeEvenOdd(self, head):

        # Corner case
        if (self.head == None):
            return None

        # Initialize first nodes of
        # even and odd lists
        odd = self.head
        even = self.head.next

        # Remember the first node of even list so
        # that we can connect the even list at the
        # end of odd list.
        evenFirst = even

        while (1 == 1):

            # If there are no more nodes,
            # then connect first node of even
            # list to the last node of odd list
            if (odd == None or even == None or
                    (even.next) == None):
                odd.next = evenFirst
                break

            # Connecting odd nodes
            odd.next = even.next
            odd = even.next

            # If there are NO more even nodes
            # after current odd.
            if (odd.next == None):
                even.next = None
                odd.next = evenFirst
                break

            # Connecting even nodes
            even.next = odd.next
            even = odd.next
        return head

    # A utility function to print a linked list
    def printlist(self, node):
        while (node != None):
            print(node.data, end="")
            print("->", end="")
            node = node.next
        print("NULL")

    # Function to insert a new node
    # at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


# Driver code
ll = LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print("Given Linked List")
ll.printlist(ll.head)

start = ll.rearrangeEvenOdd(ll.head)

print("\nModified Linked List")
ll.printlist(start)





# ...............................................ans 6............................................
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
		# allocate node and put the data
		new_node = Node(new_data)

		# Make next of new node as head
		new_node.next = self.head

		# move the head to point to the new Node
		self.head = new_node

	# Utility function to print it the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next

	# This function rotates a linked list counter-clockwise and
	# updates the head. The function assumes that k is smaller
	# than size of linked list. It doesn't modify the list if
	# k is greater than of equal to size
	def rotate(self, k):
		if k == 0:
			return

		# Let us understand the below code for example k = 4
		# and list = 10->20->30->40->50->60
		current = self.head

		# current will either point to kth or NULL after
		# this loop
		# current will point to node 40 in the above example
		count = 1
		while(count < k and current is not None):
			current = current.next
			count += 1

		# If current is None, k is greater than or equal
		# to count of nodes in linked list. Don't change
		# the list in this case
		if current is None:
			return

		# current points to kth node. Store it in a variable
		# kth node points to node 40 in the above example
		kthNode = current

		# current will point to last node after this loop
		# current will point to node 60 in above example
		while(current.next is not None):
			current = current.next

		# Change next of last node to previous head
		# Next of 60 is now changed to node 10
		current.next = self.head

		# Change head to (k + 1)th node
		# head is not changed to node 50
		self.head = kthNode.next

		# change next of kth node to NULL
		# next of 40 is not NULL
		kthNode.next = None


# Driver program to test above function
llist = LinkedList()

# Create a list 10->20->30->40->50->60
for i in range(60, 0, -10):
	llist.push(i)

print "Given linked list"
llist.printList()
llist.rotate(4)

print "\nRotated Linked list"
llist.printList()




# ......................................ans 6....................................
head = None

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

# to get size of LinkedList


def sizeOfLL(head):
	count = 0
	while (head != None):
		count = count + 1
		head = head.next

	return count


def nextLargerLL(head):
	# get size of LinkedList
	count = sizeOfLL(head)
	# make size of ans array equal to size of LL i.e
	# number of nodes in LL
	ans = [None]*count
	# k is for index of ans array
	k = 0
	# j will be one step ahead of head node that will
	# check the greater node
	j = None
	# temp is for temporary storing the greater node
	temp = 0

	while (head != None):
		# if head.next is None it means there will be
		# no greater node than head afterwards so add 0
		# to ans array
		if (head.next == None):
			ans[k] = 0
			break

		# j is one step ahead of head
		j = head.next
		# if head.val is smaller than j.val so add
		# j.val to ans array and increment index (k)
		if (head.val < j.val):
			ans[k] = j.val
			k += 1

		elif (head.val >= j.val): # if head.val is greater
			# than or equal to j.val
			while (
					j != None and head.val >= j.val): # search j.val such
				# that it is greater
				# than head.val
				j = j.next

			# if j is not equal to None it means we
			#	 have got a value in LL which is greater
			#	 than head so add j.val to ans array
			#	 increment k after adding j.val

			if (j != None):
				ans[k] = j.val
				k += 1

			else: # it means we have not found any
				# value which is greater than head so
				# add 0 to ans array and increment
				# index
				ans[k] = 0
				k += 1

		else:
			ans[k] = 0
			k += 1

		head = head.next

	return ans


def push(new_data):
	global head
	# allocate node None
	new_node = ListNode(new_data)

	# link the old list of the new node None
	new_node.next = head

	# move the head to point to the new node None
	head = new_node


# Utility function to print the linked list
def printList():
	print(nextLargerLL(head))


# driver code
if __name__ == '__main__':
	push(5)
	push(0)
	push(3)
	push(1)
	push(2)

	# Function Call
	nextLargerLL(head)
	printList()




# ..................................ans 8............................................
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

# Function to create Node
def getNode(data):
	temp = ListNode(data)
	temp.next = None
	return temp

# Function to print the Linked List
def printList(head):
	while (head.next):
		print(head.val, end=' -> ')
		head = head.next
	print(head.val, end='')

# Function that removes continuous nodes
# whose sum is K
def removeZeroSum(head, K):

	# Root node initialise to 0
	root = ListNode(0)

	# Append at the front of the given
	# Linked List
	root.next = head

	# Map to store the sum and reference
	# of the Node
	umap = dict()

	umap[0] = root

	# To store the sum while traversing
	sum = 0

	# Traversing the Linked List
	while (head != None):

		# Find sum
		sum += head.val

		# If found value with (sum - K)
		if ((sum - K) in umap):

			prev = umap[sum - K]
			start = prev

			# Delete all the node
			# traverse till current node
			aux = sum

			# Update sum
			sum = sum - K

			# Traverse till current head
			while (prev != head):
				prev = prev.next
				aux += prev.val
				if (prev != head):
					umap.remove(aux)

			# Update the start value to
			# the next value of current head
			start.next = head.next

		# If (sum - K) value not found
		else:
			umap[sum] = head

		head = head.next

	# Return the value of updated
	# head node
	return root.next


# Driver Code
if __name__ == '__main__':

	# Create Linked List
	head = getNode(1)
	head.next = getNode(2)
	head.next.next = getNode(-3)
	head.next.next.next = getNode(3)
	head.next.next.next.next = getNode(1)

	# Given sum K
	K = 5

	# Function call to get head node
	# of the updated Linked List
	head = removeZeroSum(head, K)

	# Print the updated Linked List
	if(head != None):
		printList(head)

