# ..................................ans 1.......................................
#Stack using list
stack = []

#Function to print top element of stack
def top(stack):
  if stack != []:
    print(stack[-1]  + " is top element")
  else:
    print("Stack Empty!!!")

#Function to print size of stack
def size(stack):
  print("Size of stack is " + str(len(stack)))

#Function to check if a stack is empty
def empty(stack):
  if stack == []:
    print("True")
  else:
    print("False")

# append() function is used to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

size(stack)

print(stack)

top(stack)

# pop() function to pop element from stack in LIFO order
print(stack.pop() + " is popped")

print(stack)

empty(stack)

print(stack.pop() + " is popped")
print(stack.pop() + " is popped")

print(stack)

empty(stack)





# ............................................ans 2...........................................
# Python program to demonstrate queue implementation using list

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# print(queue.pop(0))
# will raise and IndexError as the queue is now empty
