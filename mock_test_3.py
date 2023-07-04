# ......................................ans 1.............................................
def evn_list(lst : list):
    lst = [x for x in lst if x%2==0]
    return lst

# ans = evn_list([1,2,3,4,5,78])
# print(ans)

# .......................................ans 2................................................
from time import time

def timer(func):
	# This function shows the execution time of the function object passed
	def wrap_func(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
		return result
	return wrap_func


@timer
def long_time(n):
    for i in range(n):
	    for j in range(100000):
		    i*j

# long_time(50)

# ....................................................ans 3................................................
def calculate_mean(numbers: list):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

data = [10, 15, 20, 25, 30]
mean_value = calculate_mean(data)
print("Mean:", mean_value)


# ..............................................ans 4....................................................
from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value

sample1 = [5, 10, 15, 20, 25]
sample2 = [10, 20, 30, 40, 50]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)

