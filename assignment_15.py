# Function to print element and NGE pair for all elements of list
def printNGE(arr):

	for i in range(0, len(arr), 1):

		next = -1
		for j in range(i+1, len(arr), 1):
			if arr[i] < arr[j]:
				next = arr[j]
				break

		print(str(arr[i]) + " -- " + str(next))


# Driver program to test above function
arr = [11, 13, 21, 3]
printNGE(arr)





# .........................................ans 2...........................................
# Python 3 implementation of simple algorithm to find smaller element on left side

# Prints smaller elements on left side of every element
def printPrevSmaller(arr, n):
    # Always print empty or '_' for first element
    print("_, ", end="")

    # Start from second element
    for i in range(1, n):

        # look for smaller element
        # on left of 'i'
        for j in range(i - 1, -2, -1):

            if (arr[j] < arr[i]):
                print(arr[j], ", ",
                      end="")
                break

        # If there is no smaller
        # element on left of 'i'
        if (j == -1):
            print("_, ", end="")


# Driver program to test insertion
# sort
arr = [1, 3, 0, 2, 5]
n = len(arr)
printPrevSmaller(arr, n)






# ........................................ans 3 ......................................
# Program to implement a stack using two queue
from _collections import deque


class Stack:

	def __init__(self):

		# Two inbuilt queues
		self.q1 = deque()
		self.q2 = deque()

	def push(self, x):

		# Push x first in empty q2
		self.q2.append(x)

		# Push all the remaining
		# elements in q1 to q2.
		while (self.q1):
			self.q2.append(self.q1.popleft())

		# swap the names of two queues
		self.q1, self.q2 = self.q2, self.q1

	def pop(self):

		# if no elements are there in q1
		if self.q1:
			self.q1.popleft()

	def top(self):
		if (self.q1):
			return self.q1[0]
		return None

	def size(self):
		return len(self.q1)


# Driver Code
if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)

	print("current size: ", s.size())
	print(s.top())
	s.pop()
	print(s.top())
	s.pop()
	print(s.top())

	print("current size: ", s.size())




# .........................................ans 4............................................
# Python program to reverse a stack using recursion

# Below is a recursive function that inserts an element at the bottom of a stack.

def insertAtBottom(stack, item):
	if isEmpty(stack):
		push(stack, item)
	else:
		temp = pop(stack)
		insertAtBottom(stack, item)
		push(stack, temp)

# Below is the function that reverses the given stack using insertAtBottom()

def reverse(stack):
	if not isEmpty(stack):
		temp = pop(stack)
		reverse(stack)
		insertAtBottom(stack, temp)

# Below is a complete running program for testing above functions.

# Function to create a stack. It initializes size of stack as 0

def createStack():
	stack = []
	return stack

# Function to check if the stack is empty

def isEmpty(stack):
	return len(stack) == 0

# Function to push an item to stack

def push(stack, item):
	stack.append(item)

# Function to pop an item from stack

def pop(stack):

	# If stack is empty then error
	if(isEmpty(stack)):
		print("Stack Underflow ")
		exit(1)

	return stack.pop()

# Function to print the stack


def prints(stack):
	for i in range(len(stack)-1, -1, -1):
		print(stack[i], end=' ')
	print()

# Driver Code


stack = createStack()
push(stack, str(4))
push(stack, str(3))
push(stack, str(2))
push(stack, str(1))
print("Original Stack ")
prints(stack)

reverse(stack)

print("Reversed Stack ")
prints(stack)







# .............................................ans 5...........................................
# Python program to reverse a string using stack

# Function to create an empty stack.
# It initializes size of stack as 0


def createStack():
	stack = []
	return stack

# Function to determine the size of the stack


def size(stack):
	return len(stack)

# Stack is empty if the size is 0


def isEmpty(stack):
	if size(stack) == 0:
		return True

# Function to add an item to stack .
# It increases size by 1


def push(stack, item):
	stack.append(item)

# Function to remove an item from stack.
# It decreases size by 1


def pop(stack):
	if isEmpty(stack):
		return
	return stack.pop()

# A stack based function to reverse a string


def reverse(string):
	n = len(string)

	# Create a empty stack
	stack = createStack()

	# Push all characters of string to stack
	for i in range(0, n, 1):
		push(stack, string[i])

	# Making the string empty since all characters are saved in stack
	string = ""

	# Pop all characters of string and put them back to string
	for i in range(0, n, 1):
		string += pop(stack)

	return string


# Driver program to test above functions
string = "GeeksQuiz"
string = reverse(string)
print("Reversed string is " + string)





# ...............................................ans6..........................................
# Python program to evaluate value of a postfix expression


# Class to convert the expression
class Evaluate:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        # This array is used a stack
        self.array = []

    # Check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # The main function that converts given infix expression
    # to postfix expression
    def evaluatePostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:

            # If the scanned character is an operand
            # (number here) push it to the stack
            if i.isdigit():
                self.push(i)

            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))

        return int(self.pop())


# Driver code
if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))

    # Function call
    print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))






# ................................................ans 7.......................................
# Class to make a Node
class Node:
	# Constructor which assign argument to nade's value
	def __init__(self, value):
		self.value = value
		self.next = None

	# This method returns the string representation of the object.
	def __str__(self):
		return "Node({})".format(self.value)

	# __repr__ is same as __str__
	__repr__ = __str__


class Stack:
	# Stack Constructor initialise top of stack and counter.
	def __init__(self):
		self.top = None
		self.count = 0
		self.minimum = None

	# This method returns the string representation of the object (stack).
	def __str__(self):
		temp = self.top
		out = []
		while temp:
			out.append(str(temp.value))
			temp = temp.next
		out = '\n'.join(out)
		return ('Top {} \n\nStack :\n{}'.format(self.top, out))

	# __repr__ is same as __str__
	__repr__ = __str__

	# This method is used to get minimum element of stack
	def getMin(self):
		if self.top is None:
			return "Stack is empty"
		else:
			print("Minimum Element in the stack is: {}" .format(self.minimum))

	# Method to check if Stack is Empty or not

	def isEmpty(self):
		# If top equals to None then stack is empty
		if self.top == None:
			return True
		else:
			# If top not equal to None then stack is empty
			return False

	# This method returns length of stack
	def __len__(self):
		self.count = 0
		tempNode = self.top
		while tempNode:
			tempNode = tempNode.next
			self.count += 1
		return self.count

	# This method returns top of stack
	def peek(self):
		if self.top is None:
			print("Stack is empty")
		else:
			if self.top.value < self.minimum:
				print("Top Most Element is: {}" .format(self.minimum))
			else:
				print("Top Most Element is: {}" .format(self.top.value))

	# This method is used to add node to stack
	def push(self, value):
		if self.top is None:
			self.top = Node(value)
			self.minimum = value

		elif value < self.minimum:
			temp = (2 * value) - self.minimum
			new_node = Node(temp)
			new_node.next = self.top
			self.top = new_node
			self.minimum = value
		else:
			new_node = Node(value)
			new_node.next = self.top
			self.top = new_node
		print("Number Inserted: {}" .format(value))

	# This method is used to pop top of stack
	def pop(self):
		if self.top is None:
			print("Stack is empty")
		else:
			removedNode = self.top.value
			self.top = self.top.next
			if removedNode < self.minimum:
				print("Top Most Element Removed :{} " .format(self.minimum))
				self.minimum = ((2 * self.minimum) - removedNode)
			else:
				print("Top Most Element Removed : {}" .format(removedNode))


# Driver program to test above class
if __name__ == '__main__':

stack = Stack()

# Function calls
stack.push(3)
stack.push(5)
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()
stack.pop()
stack.getMin()
stack.pop()
stack.peek()






# .................................................ans8.......................................
# Python3 implementation of the approach

# Function to return the maximum
# water that can be stored
def maxWater(arr, n):

	# To store the maximum water
	# that can be stored
	res = 0

	# For every element of the array
	for i in range(1, n - 1):

		# Find the maximum element on its left
		left = arr[i]
		for j in range(i):
			left = max(left, arr[j])

		# Find the maximum element on its right
		right = arr[i]

		for j in range(i + 1, n):
			right = max(right, arr[j])

		# Update the maximum water
		res = res + (min(left, right) - arr[i])

	return res


# Driver code
if __name__ == "__main__":

	arr = [0, 1, 0, 2, 1, 0,
		1, 3, 2, 1, 2, 1]
	n = len(arr)

	print(maxWater(arr, n))

