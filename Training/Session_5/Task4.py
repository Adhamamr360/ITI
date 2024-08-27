import numpy as np
from scipy import stats

# Group A scores
group_a_scores = [85, 90, 88, 92, 78, 95, 89, 91, 82, 87]
# Group B scores
group_b_scores = [78, 82, 80, 85, 76, 88, 84, 89, 83, 79]

# Calculate the mean and standard deviation for each group
mean_a = np.mean(group_a_scores)
mean_b = np.mean(group_b_scores)
std_a = np.std(group_a_scores, ddof=1)
std_b = np.std(group_b_scores, ddof=1)

# Print the means and standard deviations
print(f"Mean of Group A: {mean_a}, Std of Group A: {std_a}")
print(f"Mean of Group B: {mean_b}, Std of Group B: {std_b}")

# Independent t-test
t_statistic, p_value = stats.ttest_ind(group_a_scores, group_b_scores)

# Print the test results
print(f"T-statistic: {t_statistic}, P-value: {p_value}")

# Interpret the results
alpha = 0.05  # Significance level

if p_value < alpha:
    print("There is a significant difference in mean exam scores between the two groups.")
else:
    print("There is no significant difference in mean exam scores between the two groups.")
