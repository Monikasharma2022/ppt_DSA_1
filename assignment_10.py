def subsetSums(arr, l, r, sum=0):

	# Print current subset
	if l > r:
		print(sum, end=" ")
		return

	# Subset including arr[l]
	subsetSums(arr, l + 1, r, sum + arr[l])

	# Subset excluding arr[l]
	subsetSums(arr, l + 1, r, sum)


# Driver code
arr = [5, 4, 3]
n = len(arr)
subsetSums(arr, 0, n - 1)