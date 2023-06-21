# .....................................ans1..............................
'''NFG function to find the next greater frequency
element for each element in the array'''


def NFG(a, n):

	if (n <= 0):
		print("List empty")
		return []

	# stack data structure to store the position
	# of array element
	stack = [0]*n

	# freq is a dictionary which maintains the
	# frequency of each element
	freq = {}
	for i in a:
		freq[a[i]] = 0
	for i in a:
		freq[a[i]] += 1

	# res to store the value of next greater
	# frequency element for each element
	res = [0]*n

	# initialize top of stack to -1
	top = -1

	# push the first position of array in the stack
	top += 1
	stack[top] = 0

	# now iterate for the rest of elements
	for i in range(1, n):

		''' If the frequency of the element which is
			pointed by the top of stack is greater
			than frequency of the current element
			then push the current position i in stack'''
		if (freq[a[stack[top]]] > freq[a[i]]):
			top += 1
			stack[top] = i

		else:
			''' If the frequency of the element which
			is pointed by the top of stack is less
			than frequency of the current element, then
			pop the stack and continuing popping until
			the above condition is true while the stack
			is not empty'''

			while (top > -1 and freq[a[stack[top]]] < freq[a[i]]):
				res[stack[top]] = a[i]
				top -= 1

			# now push the current element
			top += 1
			stack[top] = i

	'''After iterating over the loop, the remaining
	position of elements in stack do not have the
	next greater element, so print -1 for them'''
	while (top > -1):
		res[stack[top]] = -1
		top -= 1

	# return the res list containing next
	# greater frequency element
	return res


# Driver Code
print(NFG([1, 1, 2, 3, 4, 2, 1], 7))



# .......................................ans2............................................
# Python program to sort a stack using auxiliary stack.

# This function return the sorted stack
def sortStack(stack):
    tmpStack = createStack()
    while (isEmpty(stack) == False):

        # pop out the first element
        tmp = top(stack)
        pop(stack)

        # while temporary stack is not empty and top of stack is lesser than temp
        while (isEmpty(tmpStack) == False and
               int(top(tmpStack)) < int(tmp)):
            # pop from temporary stack and push it to the input stack
            push(stack, top(tmpStack))
            pop(tmpStack)

        # push temp in temporary of stack
        push(tmpStack, tmp)

    return tmpStack


# Below is a complete running program for testing above function.

# Function to create a stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack


# Function to check if the stack is empty
def isEmpty(stack):
    return len(stack) == 0


# Function to push a item to stack
def push(stack, item):
    stack.append(item)


# Function to get top item of stack
def top(stack):
    p = len(stack)
    return stack[p - 1]


# Function to pop an item from stack
def pop(stack):
    # If stack is empty then error
    if (isEmpty(stack)):
        print("Stack Underflow ")
        exit(1)

    return stack.pop()


# Function to print the stack
def prints(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=' ')
    print()


# Driver Code
stack = createStack()
push(stack, str(34))
push(stack, str(3))
push(stack, str(31))
push(stack, str(98))
push(stack, str(92))
push(stack, str(23))

print("Sorted numbers are: ")
sortedst = sortStack(stack)
prints(sortedst)





# .........................................ans3 ................................................
import math

st = []
st.append('1')
st.append('2')
st.append('3')
st.append('4')
st.append('5')
st.append('6')
st.append('7')

v = []

while (len(st) > 0):
    v.append(st[0])
    del st[0]

n = len(v)

if n % 2 == 0:
    target = math.floor(n / 2)
    for i in range(0, n):
        if i == target:
            continue
        st.append(v[i])
else:
    target = math.floor(n / 2)
    for i in range(0, n):
        if i == target:
            continue
        st.append(v[i])

print("Printing stack after deletion of middle:", end=" ")

while (len(st) > 0):
    p = st[0]
    del st[0]
    print(p, end=" ")





# .............................................ans 4........................................
# Python Program to check if a queue of first n natural number can be sorted using a stack
from queue import Queue


# Function to check if given queue element can be sorted into another queue using a stack.
def checkSorted(n, q):
    st = []
    expected = 1
    fnt = None

    # while given Queue is not empty.
    while (not q.empty()):
        fnt = q.queue[0]
        q.get()

        # if front element is the expected element
        if (fnt == expected):
            expected += 1

        else:

            # if stack is empty, put the element
            if (len(st) == 0):
                st.append(fnt)

            # if top element is less than element which need to be puted, then return false.
            elif (len(st) != 0 and st[-1] < fnt):
                return False

            # else put into the stack.
            else:
                st.append(fnt)

        # while expected element are coming from stack, pop them out.
        while (len(st) != 0 and
               st[-1] == expected):
            st.pop()
            expected += 1

    # if the final expected element value is equal to initial Queue size and the stack is empty.
    if (expected - 1 == n and len(st) == 0):
        return True

    return False


# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.put(5)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)

    n = q.qsize()

    if checkSorted(n, q):
        print("Yes")
    else:
        print("No")



# ...................................................ans 5.................................................
# Python3 program to reverse the number using a stack

# Stack to maintain order of digits
st = [];


# Function to push digits into stack
def push_digits(number):
    while (number != 0):
        st.append(number % 10);
        number = int(number / 10);


# Function to reverse the number
def reverse_number(number):
    # Function call to push number's digits to stack
    push_digits(number);

    reverse = 0;
    i = 1;

    # Popping the digits and forming the reversed number
    while (len(st) > 0):
        reverse = reverse + (st[len(st) - 1] * i);
        st.pop();
        i = i * 10;

    # Return the reversed number formed
    return reverse;


# Driver Code
number = 39997;

# Function call to reverse number
print(reverse_number(number));




# .........................................ans6.........................................
from collections import deque

def reverse_first_k(q, k):
	solve(q, k)
	s = len(q) - k
	for _ in range(s):
		x = q.popleft()
		q.append(x)
	return q

def solve(q, k):
	if k == 0:
		return
	e = q.popleft()
	solve(q, k - 1)
	q.append(e)

# Driver code
queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
k = 5
queue = reverse_first_k(queue, k)

# Printing queue
while queue:
	print(queue.popleft(), end=' ')





# ................................................ans7........................................
# Python3 program to remove consecutive same words

# Function to find the size of manipulated sequence
def removeConsecutiveSame(v):
    n = len(v)

    # Start traversing the sequence
    i = 0
    while (i < n - 1):

        # Compare the current string with next one Erase both if equal
        if ((i + 1) < len(v)) and (v[i] == v[i + 1]):

            # Erase function delete the element and also shifts other element that's why i is not updated
            v = v[:i]
            v = v[:i]

            # Update i, as to check from previous element again
            if (i > 0):
                i -= 1

            # Reduce sequence size
            n = n - 2

        # Increment i, if not equal
        else:
            i += 1

    # Return modified size
    return len(v[:i - 1])


# Driver Code
if __name__ == '__main__':
    v = ["tom", "jerry", "jerry", "tom"]
    print(removeConsecutiveSame(v))




# ...............................................ans 8...........................................
# Python program to find the difference b/w left and right smaller element of every element in the array

# Function to fill left smaller element for every element of arr[0..n-1]. These values are filled in SE[0..n-1]
def leftsmaller(arr, n, SE):
    # create an empty stack
    sta = []
    # Traverse all array elements compute nearest smaller elements of every element
    for i in range(n):

        # Keep removing top element from S while the top element is greater than or equal to arr[i]
        while (sta != [] and sta[len(sta) - 1] >= arr[i]):
            sta.pop()

        # Store the smaller element of current element
        if (sta != []):
            SE[i] = sta[len(sta) - 1]
        # If all elements in S were greater than arr[i]
        else:
            SE[i] = 0

        # push this element
        sta.append(arr[i])


# Function returns maximum difference b/w Left & right smaller element
def findMaxDiff(arr, n):
    ls = [0] * n  # to store left smaller elements
    rs = [0] * n  # to store right smaller elements

    # find left smaller elements of every element
    leftsmaller(arr, n, ls)

    # find right smaller element of every element by sending reverse of array
    leftsmaller(arr[::-1], n, rs)

    # find maximum absolute difference b/w LS & RRS In the reversed array right smaller for arr[i] is stored at RRS[n-i-1]
    res = -1
    for i in range(n):
        res = max(res, abs(ls[i] - rs[n - 1 - i]))
    # return maximum difference b/w LS & RRS
    return res


# Driver Program
if __name__ == '__main__':
    arr = [2, 4, 8, 7, 7, 9, 3]
    print
    "Maximum Diff :", findMaxDiff(arr, len(arr))

