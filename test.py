# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.

def pushZerosToEnd(arr, n):
    count = 0  # Count of non-zero elements
    for i in range(n):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1

