import matplotlib.pyplot as plt

# Sample data
data_set_1 = [1, 2, 3, 4, 5]
data_set_2 = [2, 3, 5, 7, 11, 13]

# Processing for data_set_1
sum_data_set_1 = sum(data_set_1)
average_data_set_1 = sum_data_set_1 / len(data_set_1)
squared_deviation_1 = [(x - average_data_set_1) ** 2 for x in data_set_1]
variance_data_set_1 = sum(squared_deviation_1) / len(data_set_1)

# Plotting for data_set_1
plt.figure(figsize=(8, 4))
plt.plot(data_set_1, label="Data Set 1")
plt.axhline(y=average_data_set_1, color='r', linestyle='-', label=f"Average 1 = {average_data_set_1:.2f}")
plt.title(f"Variance for Data Set 1 = {variance_data_set_1:.2f}")
plt.legend()
plt.show()

# Processing for data_set_2
sum_data_set_2 = sum(data_set_2)
average_data_set_2 = sum_data_set_2 / len(data_set_2)
squared_deviation_2 = [(x - average_data_set_2) ** 2 for x in data_set_2]
variance_data_set_2 = sum(squared_deviation_2) / len(data_set_2)

# Plotting for data_set_2
plt.figure(figsize=(8, 4))
plt.plot(data_set_2, label="Data Set 2")
plt.axhline(y=average_data_set_2, color='r', linestyle='-', label=f"Average 2 = {average_data_set_2:.2f}")
plt.title(f"Variance for Data Set 2 = {variance_data_set_2:.2f}")
plt.legend()
plt.show()

# TODO Can you think of a way to make the code more reusable?