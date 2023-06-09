class Solution:

# .....................ans 1...................
    def div_of_2(self, num):
        if num==1:
            return True
        if (num<1 or num%2!=0):
            return False
        return self.div_of_2(num//2)



# .......................ans 2..........................
    def sum_n_no(self, num):
        if (num == 1):
            return 1
        if num <0:
            return "please input a positive number"
        return num + self.sum_n_no(num-1)


# ...........................ans 3........................
    def fact(self, num):
        if num == 0:
            return 1
        if num <0:
            return "please input a positive number"
        return num * self.fact(num-1)



# ......................ans 4..........................
    def powr(self, num, exp):
        if exp == 0:
            return 1
        return num * self.powr(num, exp-1)


# ......................ans 5........................
    def findMaxRec(self, arr, n):
        if (n == 1):
            return arr[0]
        return max(arr[n - 1], self.findMaxRec(arr, n - 1))


# ...............ans 6......................
    def nth_ap(self, a, d, N):
        if N==1:
            return a
        return d + self.nth_ap(a, d, N-1)



# ...................ans 7.....................
# Function to swap two characters in a character array
    def swap(self, ch, i, j):
        temp = ch[i]
        ch[i] = ch[j]
        ch[j] = temp


    # Recursive function to generate all permutations of a string
    def permutations(self, ch, curr_index=0):
        if curr_index == len(ch) - 1:
            print(''.join(ch))

        for i in range(curr_index, len(ch)):
            self.swap(ch, curr_index, i)
            self.permutations(ch, curr_index + 1)
            self.swap(ch, curr_index, i)


# ..............ans 8...................
    def Prod_arr(self, arr, n):
        if n==1:
            return arr[0]
        return arr[n-1] * self.Prod_arr(arr, n-1)

obj = Solution()
ans = obj.permutations(list("ABC"))
print(ans)