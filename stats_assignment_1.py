# 1--------------------------------------------> Avg of given data
def Average(lst):
	return sum(lst) / len(lst)

# Driver Code
# region_A =  [10, 15, 12, 8, 14]
# region_B =  [18, 20, 16, 22, 25]
#
# average = Average(region_A)
# print(average)




# 2.--------------------------------------------> Mode of given data
def get_mode(n_num):
	from collections import Counter
	data = Counter(n_num)
	get_mode = dict(data)
	mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

	if len(mode) == len(n_num):
		get_mode = "No mode found"
	else:
		get_mode = "Mode is: " + ', '.join(map(str, mode))

	print(get_mode)


# get_mode([4, 5, 2, 3, 5, 4, 3, 2, 4, 5])



# 3.--------------------------------------------> median of the given data
def mediaN(lst:list):
	#sort list in ascending order
	lst.sort()

	#if length of list is even
	if len(lst) % 2 == 0:
		mid = int(len(lst)/2)
		n = lst[mid]+lst[mid-1]
		median = float(n)/2
		return median

	# if length of list is odd
	if len(lst) % 2 != 0:
		mid = len(lst)//2
		return lst[mid]


# department_A = [5000, 6000, 5500, 7000]
# department_B = [4500, 5500, 5800, 6000, 5200]
# median_A = mediaN(department_A)
# median_B = mediaN(department_B)
# print(f"median salary of Department A is {median_A} and Department B is {median_B}")



# 4.--------------------------------------------> range of the given data
def stat_range(lst):
	lst.sort()
	return (lst[-1] - lst[0])


# data = [25.5, 24.8, 26.1, 25.3, 24.9]
# range = stat_range(data)
# print("Range of the given data is: ", range)




# 5.--------------------------------------------> perform t-test
# Before conducting the two-sample t-test using Python let us discuss the assumptions of this parametric test.
# Basically, there are three assumptions that we can make regarding the data groups:
#
# Whether the two samples data groups are independent.
# Whether the data elements in respective groups follow any normal distribution.
# Whether the given two samples have similar variances. This assumption is also known as the homogeneity assumption.


# Python program to display variance of data groups
def t_test(group1, group2):
	import scipy.stats as stats
	import numpy as np

	# Print the variance of both data groups
	print("var of Group1 is " ,np.var(group1), "and var of Group2 is ", np.var(group2))
	if np.var(group1) >= np.var(group2):
		if np.var(group1)/np.var(group2) >=1 and np.var(group1)/np.var(group1)<= 4:
			# Perform the two sample t-test with equal variances
			tc, p = stats.ttest_ind(a=group1, b=group2, equal_var=True)

			# interpret p-value
			alpha = 0.05
			print("p value is " + str(p))
			if p <= alpha:
				print('Dependent (reject H0)')
			else:
				print('Independent (H0 holds true)')


	if np.var(group2) >= np.var(group1):
		if np.var(group2)/np.var(group1) >=1 and np.var(group1)/np.var(group1)<= 4:
			# Perform the two sample t-test with equal variances
			tc, p = stats.ttest_ind(a=group1, b=group2, equal_var=True)

			# interpret p-value
			alpha = 0.05
			print("p value is " + str(p))
			if p <= alpha:
				print('significant diff btw means (reject H0)')
			else:
				print('not significant diff btw means (H0 holds true)')




# Creating data groups
# Group_A = [85, 90, 92, 88, 91]
# Group_B = [82, 88, 90, 86, 87]
# t_test(Group_A, Group_B)




# 6.---------------------------------------> Calculate the correlation coefficient between advertising expenditure and sales.
def corr_coff(x, y):
	corr_matrix = np.corrcoef(x, y)
	corr = corr_matrix[0][1]
	return corr

# import numpy as np
# advertising_expenditure = np.array([10, 15, 12, 8, 14])
# sales = np.array([25, 30, 28, 20, 26])
# corr = corr_coff(advertising_expenditure, sales)
# print("Calculate the correlation coefficient between advertising expenditure and sales is: ", corr)






#7.--------------------->
def standard_deviation(heights):
	"""
	Calculates the standard deviation of a list of heights.

	Args:
	heights: A list of heights.

	Returns:
	The standard deviation of the heights.
	"""

	import statistics
	mean = statistics.mean(heights)
	squared_deviations = []
	for height in heights:
		deviation = height - mean
		squared_deviation = deviation ** 2
		squared_deviations.append(squared_deviation)

	variance = statistics.mean(squared_deviations)
	standard_deviation = variance ** 0.5

	return standard_deviation


# if __name__ == "__main__":
# 	heights = [160, 170, 165, 155, 175, 180, 170]
# 	standard_deviation = standard_deviation(heights)
# 	print(standard_deviation)




# 8--------------------------------->linear regression
def linear_regression(tenure, satisfaction):
	"""
	Performs a linear regression analysis to predict job satisfaction based on employee tenure.

	Args:
	tenure: A list of employee tenures.
	satisfaction: A list of job satisfaction scores.

	Returns:
	A tuple of the coefficients and intercept of the linear regression model.
	"""

	from sklearn.linear_model import LinearRegression

	# Create the linear regression model
	model = LinearRegression()
	model.fit(tenure, satisfaction)

	# Return the coefficients and intercept
	return model.coef_, model.intercept_


# if __name__ == "__main__":
# 	import numpy as np
#
# 	tenure = np.array([2, 3, 5, 4, 6, 2, 4]).reshape(-1,1)
# 	satisfaction = np.array([7, 8, 6, 9, 5, 7, 6]).reshape(-1,1)
#
# 	# Perform the linear regression analysis
# 	coefficients, intercept = linear_regression(tenure, satisfaction)
#
# 	# Print the coefficients
# 	print("Coefficients:", coefficients)
# 	print("Intercept:", intercept)






# 9. ---------------------------------------------->ANOVA
import numpy as np
from scipy import stats

def anova(medication_a, medication_b):
	"""
	Performs an analysis of variance (ANOVA) to determine if there is a significant difference in the mean recovery times between the two medications.

	Args:
	medication_a: A list of recovery times for medication A.
	medication_b: A list of recovery times for medication B.

	Returns:
	A tuple of the F-statistic and p-value of the ANOVA test.
	"""

	# Calculate the mean recovery times for each medication.
	mean_a = np.mean(medication_a)
	mean_b = np.mean(medication_b)

	# Calculate the variance of the recovery times for each medication.
	variance_a = np.var(medication_a)
	variance_b = np.var(medication_b)

	# Calculate the F-statistic.
	f_statistic = (variance_a / variance_b)

	# Calculate the p-value.
	p_value = stats.f.sf(f_statistic, dfn = len(medication_a) - 1, dfd = len(medication_b) - 1)

	return f_statistic, p_value


# if __name__ == "__main__":
# 	medication_a = [10, 12, 14, 11, 13]
# 	medication_b = [15, 17, 16, 14, 18]
#
# 	# Perform the ANOVA test.
# 	f_statistic, p_value = anova(medication_a, medication_b)
#
# 	# Print the F-statistic and p-value.
# 	print("F-statistic:", f_statistic)
# 	print("p-value:", p_value)




# 10 ------------------------------------------------>
def calculate_percentile(data, percentile):
  """
  Calculates the percentile of a given value in a data set.

  Args:
    data: A list of values.
    percentile: The percentile to calculate.

  Returns:
    The value at the given percentile.
  """

  data.sort()
  index = int(len(data) * percentile)

  return data[index]


# if __name__ == "__main__":
#   data = [6, 7, 7, 8, 8, 8, 8, 9, 9, 10]
#   percentile = 0.75
#
#   percentile_value = calculate_percentile(data, percentile)
#
#   print("The 75th percentile is:", percentile_value)





# 11. -------------------------------------------------->
import numpy as np
from scipy import stats

def t_test(data, mean, standard_deviation, n):
	"""
	Performs a t-test to determine if the mean of a sample differs significantly from a given value.

	Args:
	data: A list of values.
	mean: The mean value to compare against.
	standard_deviation: The standard deviation of the sample.
	n: The number of samples.

	Returns:
	The t-statistic and p-value of the t-test.
	"""

	t_statistic = (Average(data) - mean) / (standard_deviation / np.sqrt(n))
	p_value = 2* stats.t.sf(t_statistic, n - 1)   # returning p value for one tail so we have to multiply by 2

	return t_statistic, p_value


# if __name__ == "__main__":
# 	data = [10.2, 9.8, 10.0, 10.5, 10.3, 10.1]
# 	mean = 10
# 	standard_deviation = 0.2       # calculated with function in question 7
# 	n = 6
#
# 	t_statistic, p_value = t_test(data, mean, standard_deviation, n)
#
# 	print("t-statistic:", t_statistic)
# 	print("p-value:", p_value)
#




# 12.--------------------------------------------> perform chi-square test
from scipy.stats import chi2_contingency

def chi_2(data):
	stat, p, dof, expected = chi2_contingency(data)

	# interpret p-value
	alpha = 0.05
	print("p value is " + str(p))
	if p <= alpha:
		print('Dependent (reject H0)')
	else:
		print('Independent (H0 holds true)')


# data = [[100, 120, 110, 90, 95], [80, 85, 90, 95, 100]]
# chi_2(data)





# 13-------------------------------------------->
import numpy as np
from scipy.stats import t

def calculate_confidence_interval(data, confidence_level):
	"""
	Calculates the 95% confidence interval for the population mean.

	Args:
	data: The data to be used to calculate the confidence interval.
	confidence_level: The confidence level of the confidence interval.

	Returns:
	The 95% confidence interval for the population mean.
	"""

	sample_mean = np.mean(data)
	sample_standard_deviation = np.std(data)
	sample_size = len(data)
	t_value = t.ppf(1 - (1 - confidence_level) / 2, sample_size - 1)
	margin_of_error = t_value * sample_standard_deviation / np.sqrt(sample_size)
	confidence_interval = (
	  sample_mean - margin_of_error,
	  sample_mean + margin_of_error)

	return confidence_interval

# if __name__ == "__main__":
# 	data = [7, 9, 6, 8, 10, 7, 8, 9, 7, 8]
# 	confidence_interval = calculate_confidence_interval(data, 0.95)
# 	print(confidence_interval)





# 14.---------------------------------------------->linear regression
def linear_regression(temperature, performance):
	"""
		Performs a simple linear regression to predict performance based on temperature.

		Returns:
		The linear regression model.
		"""

	from sklearn.linear_model import LinearRegression

	# Create the linear regression model
	model = LinearRegression()
	model.fit(temperature, performance)

	# Return the coefficients and intercept
	return model.coef_, model.intercept_


# if __name__ == "__main__":
# 	import numpy as np
#
# 	temperature = np.array([20, 22, 23, 19, 21]).reshape(-1,1)
# 	performance = np.array([8, 7, 9, 6, 8]).reshape(-1,1)
#
# 	# Perform the linear regression analysis
# 	coefficients, intercept = linear_regression(temperature, performance)
#
# 	# Print the coefficients
# 	print("Coefficients:", coefficients)
# 	print("Intercept:", intercept)





# 15.--------------------------------------->Mann-Whitney U test
def mann_whitney_u(group_a, group_b):
	"""
	Performs a Mann-Whitney U test to determine if there is a significant difference in the median preferences between the two groups.

	Args:
	group_a: The data for group A.
	group_b: The data for group B.

	Returns:
	The Mann-Whitney U statistic.
	"""

	n1 = len(group_a)
	n2 = len(group_b)

	ranks = []
	for i in range(n1 + n2):
		if i < n1:
		  ranks.append(i + 1)
		else:
		  ranks.append(2 * n1 + i + 1)

	R1 = sum(ranks[i] for i in range(n1) if group_a[i] <= group_b[i])
	U = n1 * n2 - R1

	return U


# if __name__ == "__main__":
# 	group_a = [4, 3, 5, 2, 4]
# 	group_b = [3, 2, 4, 3, 3]
#
# 	U = mann_whitney_u(group_a, group_b)
#
# 	print("The Mann-Whitney U statistic is:", U)





# 16------------------------------------->interquartile range
def interquartile_range(data):
	"""
	Calculates the interquartile range (IQR) of the data.

	Args:
	data: The data to calculate the IQR for.

	Returns:
	The IQR of the data.
	"""

	sorted_data = sorted(data)
	n = len(sorted_data)

	q1 = sorted_data[n // 4]
	q3 = sorted_data[3 * n // 4]

	IQR = q3 - q1

	return IQR


# if __name__ == "__main__":
# 	data = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
#
# 	IQR = interquartile_range(data)
#
# 	print("The IQR of the data is:", IQR)






# 17---------------------------------------->kruskal walis test
def kruskal_wallis(data):
	"""
	Performs a Kruskal-Wallis test to determine if there is a significant difference in the medians of the data.

	Args:
	data: The data to perform the Kruskal-Wallis test on.

	Returns:
	The Kruskal-Wallis test statistic.
	"""

	n = len(data)
	H = 1
	for i in range(n):
		x_i = data[i]
		sum_ranks = 0
		for j in range(n):
			if x_i <= data[j]:
		  		sum_ranks += j + 1
	H += (n * sum_ranks ** 2) / (n ** 2 - 1)

	return H


# if __name__ == "__main__":
# 	data = [[0.85, 0.80, 0.82, 0.87, 0.83], [0.78, 0.82, 0.84, 0.80, 0.79], [0.90, 0.88, 0.89, 0.86, 0.87]]
#
# 	H = kruskal_wallis(data)
#
# 	print("The Kruskal-Wallis test statistic is:", H)






# 18  A company wants to analyze the effect of price on sales. The data collected is as follows:
#     Perform a simple linear regression to predict sales based on price.



# if __name__ == "__main__":
# 	import numpy as np
#
# 	price = np.array([10, 15, 12, 8, 14]).reshape(-1,1)
# 	sales = np.array([100, 80, 90, 110, 95]).reshape(-1,1)
#
# 	# Perform the linear regression analysis
# 	coefficients, intercept = linear_regression(price, sales)
#
# 	# Print the coefficients
# 	print("Coefficients:", coefficients)
# 	print("Intercept:", intercept)





# 19------------------------------------>standard error
def standard_error_of_mean(data):
	"""
	Calculates the standard error of the mean for the data.

	Args:
	data: The data to calculate the standard error of the mean for.

	Returns:
	The standard error of the mean.
	"""

	n = len(data)
	mean = sum(data) / n
	variance = sum((x - mean) ** 2 for x in data) / (n - 1)
	standard_error = math.sqrt(variance)

	return standard_error


# if __name__ == "__main__":
# 	import math
# 	data = [7, 8, 9, 6, 8, 7, 9, 7, 8, 7]
#
# 	standard_error = standard_error_of_mean(data)
#
# 	print("The standard error of the mean is:", standard_error)






# 20--------------------------------------->multiple linear regression
import numpy as np
import statsmodels.api as sm

def multiple_regression(data):
	"""
	Performs a multiple regression analysis to predict sales based on advertising expenditure.

	Args:
	data: The data to perform the multiple regression analysis on.

	Returns:
	The multiple regression model.
	"""

	advertising_expenditure = data[:, 0]
	sales = data[:, 1]

	model = sm.OLS(sales, advertising_expenditure).fit()

	return model


if __name__ == "__main__":
	data = np.array([
	[10, 25],
	[15, 30],
	[12, 28],
	[8, 20],
	[14, 26]
	])

	model = multiple_regression(data)

	print(model.summary())
