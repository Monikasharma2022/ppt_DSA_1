# ..................................ans1.............................

def FirstNonRepeat(s):
	for i in s:
		if (s.find(i, (s.find(i)+1))) == -1:
			print("First non-repeating character is found at index", s.index(i))
			break
	return

# __main__
# s = 'monikaSharma'
#
# FirstNonRepeat(s)



# ..............................................ans2..........................................
# Python program for maximum contiguous circular sum problem

# The function returns maximum circular contiguous sum in a[]
def maxCircularSum(a, n):
	# Corner Case
	if (n == 1):
		return a[0]

	# Initialize sum variable which store total sum of the array.
	sum = 0
	for i in range(n):
		sum += a[i]

	# Initialize every variable with first value of array.
	curr_max = a[0]
	max_so_far = a[0]
	curr_min = a[0]
	min_so_far = a[0]

	# Concept of Kadane's Algorithm
	for i in range(1, n):
		# Kadane's Algorithm to find Maximum subarray sum.
		curr_max = max(curr_max + a[i], a[i])
		max_so_far = max(max_so_far, curr_max)

		# Kadane's Algorithm to find Minimum subarray sum.
		curr_min = min(curr_min + a[i], a[i])
		min_so_far = min(min_so_far, curr_min)
	if (min_so_far == sum):
		return max_so_far

	# returning the maximum value
	return max(max_so_far, sum - min_so_far)


# Driver code
# a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
# n = len(a)
# print("Maximum circular sum is", maxCircularSum(a, n))





# .................................................ans3..............................................


def countStudents(students: list[int], sandwiches: list[int]) -> int:
	circularSandwiches = 0
	squareSandwiches = 0
	for i in range(len(students)):
		if students[i] == 0:
			circularSandwiches += 1
		else:
			squareSandwiches += 1
	for i in range(len(sandwiches)):
		if sandwiches[i] == 0:
			if circularSandwiches == 0:
				return squareSandwiches
			circularSandwiches -= 1
		else:
			if squareSandwiches == 0:
				return circularSandwiches
			squareSandwiches -= 1
	return circularSandwiches + squareSandwiches



# ans = countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])
# print(ans)




# .................................................ans 4.............................................

import collections
class RecentCounter:

	def __init__(self):
		self.q = collections.deque()

	def ping(self, t: int) -> int:
		self.q.append(t)

		while self.q[0] < t - 3000:
			self.q.popleft()

		return len(self.q)


# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]

# recentCounter = RecentCounter();
# recentCounter.ping(1);     # requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   # requests = [1,100], range is [-2900,100], return 2
# recentCounter.ping(3001);  # requests = [1,100,3001], range is [1,3001], return 3
# recentCounter.ping(3002);  # requests = [1,100,3001,3002], range is [2,3002], return 3





# .................................ans5.....................................

def findTheWinner(n: int, k: int) -> int:
	queue = list(range(n, 0, -1))  # Creates list of n to 1
	cur_k = k - 1
	while len(queue) != 1:
		while cur_k != 0:
			queue.insert(0, queue.pop())  # Popping front element and pushing it to the end of queue
			cur_k -= 1
		queue.pop()  # Popping the friend that looses
		cur_k = k - 1  # Resetting

	return queue.pop()  # Winner


# ans = findTheWinner(5,2)
# print(ans)




# ........................................................ans6.........................................................

from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        queue = deque()
        deck.sort(reverse=True)
        for card in deck:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)
        return queue



# obj = Solution()
# ans = obj.deckRevealedIncreasing([17,13,11,2,3,5,7])
# print(ans)



# ......................................................ans 7.............................................

class FrontMiddleBackQueue(object):

    def __init__(self):
        self.A, self.B = deque(), deque() # taking empty deques, one we`ll use for front & otherone for pushing from back.

    def pushFront(self, val):
        self.A.appendleft(val) # pushing elem from front in A.
        self.balance() # to keep a check on both queue`s size.

    def pushMiddle(self, val):
        if len(self.A) > len(self.B): # if we have more elem in A
            self.B.appendleft(self.A.pop()) # then we`ll make space in A, by pushing A`s last elem to the front of B.
        self.A.append(val) # then we will push elem at last of A.

    def pushBack(self, val):
        self.B.append(val) # pushing elem from back in B.
        self.balance() # to keep a check on both queue`s size.

    def popFront(self):
        val = self.A.popleft() if self.A else -1 # if we have anything in A, we`ll pop front from A else -1.
        self.balance() # to keep a check on both queue`s size.
        return val

    def popMiddle(self):
        val = (self.A or [-1]).pop() # if we have anything in A, we`ll pop last from A as we push at last of A else -1.
        self.balance() # to keep a check on both queue`s size.
        return val

    def popBack(self):
        val = (self.B or self.A or [-1]).pop() # as for pushing from back we push element in B, so we first try to pop from there else will check in A else -1.
        self.balance() # to keep a check on both queue`s size.
        return val

    #Our target is to keep A.size() >= B.size()
    def balance(self):
        if len(self.A) > len(self.B) + 1: # in case A is getting bigger then B
            self.B.appendleft(self.A.pop()) # we will add A`s last element in the B front
        if len(self.A) < len(self.B):  # in case B`s len is getting bigger then A`s,
            self.A.append(self.B.popleft()) # we will add B`s front to A`s rear.



# q = FrontMiddleBackQueue();
# q.pushFront(1);   # [1]
# q.pushBack(2);    #// [1,2]
# q.pushMiddle(3);  #// [1,3, 2]
# q.pushMiddle(4);  #// [1,4, 3, 2]
# q.popFront();     #// return 1 -> [4, 3, 2]
# q.popMiddle();    #// return 3 -> [4, 2]
# q.popMiddle();    #// return 4 -> [2]
# q.popBack();      #// return 2 -> []
# q.popFront();     #// return -1 -> [] (The queue is empty)




# .........................................ans 8.........................................

class DataStream:
    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.n = 0

    def consec(self, num: int) -> bool:
        if num == self.v:
            self.n += 1
        else:
            self.n = 0
        return self.n >= self.k


dataStream = DataStream(4, 3) #/value = 4, k = 3
print(dataStream.consec(4)) #// Only 1 integer is parsed, so returns False.
print(dataStream.consec(4)) #// Only 2 integers are parsed.
                      #// Since 2 is less than k, returns False.
print(dataStream.consec(4)) #// The 3 integers parsed are all equal to value, so returns True.
print(dataStream.consec(3)) #// The last k integers parsed in the stream are [4,4,3].
                      # Since 3 is not equal to value, it returns False.