# .............ans1..................
def floorSqrt(x):
    # Base cases
    if (x == 0 or x == 1):
        return x

    # Starting from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1
    result = 1
    while (result <= x):
        i += 1
        result = i * i

    return i - 1


# ......................ans2....................
def findPeak(arr, n):
    # first or last element is peak element
    if (n == 1):
        return 0
    if (arr[0] >= arr[1]):
        return 0
    if (arr[n - 1] >= arr[n - 2]):
        return n - 1

    # check for every other element
    for i in range(1, n - 1):

        # check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]):
            return i

# Driver code.
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))



# ....................ans3...........................
# Find Missing Element
def findMissing(arr, N):

	# create a list of zeroes
	temp = [0] * (N+1)

	for i in range(0, N):
		temp[arr[i] - 1] = 1

	for i in range(0, N+1):
		if(temp[i] == 0):
			ans = i + 1

	print(ans)


# Driver code
if __name__ == '__main__':
	arr = [1, 2, 3, 5]
	N = len(arr)

	# Function call
	findMissing(arr, N)



# ......................ans4......................
# Python3 code to find duplicates in O(n) time
numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr_size = len(numRay)
for i in range(arr_size):

	x = numRay[i] % arr_size
	numRay[x] = numRay[x] + arr_size

print("The repeating elements are : ")
for i in range(arr_size):
	if (numRay[i] >= arr_size*2):
		print(i, " ")




# ..................................ans5..................................
# Python program for the union of two arrays using Set
def getUnion(a, n, b, m):

	# Defining set container s
	s = set()

	# Inserting array elements in s
	for i in range(n):
		s.add(a[i])

	for i in range(m):
		s.add(b[i])
	print("Number of elements after union operation: ", len(s), "")
	print("The union set of both arrays is :" + "")

	print(s, end="") # s will contain only distinct
	# elements from array a and b


# Driver Code
if __name__ == '__main__':
	a = [1, 2, 5, 6, 2, 3, 5, 7, 3]
	b = [2, 4, 5, 6, 8, 9, 4, 6, 5, 4]

	getUnion(a, 9, b, 10)



# ....................ans6.........................
# python3 code to implement the approach

def findMin(arr, N):
    min_ele = arr[0];

    # Traversing over array to
    # find minimum element
    for i in range(N):
        if arr[i] < min_ele:
            min_ele = arr[i]

    return min_ele;


# Driver program
arr = [5, 6, 1, 2, 3, 4]
N = len(arr)

print(findMin(arr, N))

# ........................ans 7..........................
# Python 3 program to find first and
# last occurrence of an elements in
# given sorted array


# Function for finding first and last
# occurrence of an elements
def findFirstAndLast(arr, n, x):
	first = -1
	last = -1
	for i in range(0, n):
		if (x != arr[i]):
			continue
		if (first == -1):
			first = i
		last = i

	if (first != -1):
		print("First Occurrence = ", first,
			" \nLast Occurrence = ", last)
	else:
		print("Not Found")


# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 8
findFirstAndLast(arr, n, x)



# .......................ans 8..................
import sys
class Main(object) :
    @staticmethod
    def  find( arr,  target) :
        return None
    @staticmethod
    def main( args) :
        scn =  "Python-inputs"
        n = input()
        arr = [0] * (n)
        i = 0
        while (i < n) :
            arr[i] = input()
            i += 1
        target = input()
        ans = Main.find(arr, target)
        print(str(ans[0]) + " " + str(ans[1]))


if __name__=="__main__":
    Main.main(sys.argv)




