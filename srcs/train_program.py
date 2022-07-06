import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import time

def calculate_default_thetas(x, y):
	theta0 = (y[-1] - y[0]) / (x[-1] - x[0]) # a
	theta1 = y[0] - theta0 * x[0] # b
	return [theta0, theta1]

def calculate_mean_square_error(a, b, data):
	mse = 0
	for x, y in data:
		mse += (y - a * x - b) ** 2
	return mse / len(data)

def calculate_gradient(data, theta0, theta1):
	grad_x = 0
	grad_y = 0
	for x, y in data:
		grad_x += -2 * x * (y - theta0 * x - theta1)
		grad_y += -2 * (y - theta0 * x - theta1)
	return [grad_x / len(data), grad_y / len(data)]

def calculate_min_max(data):
	min_x = min(data, key = lambda x: x[0])[0]
	max_x = max(data, key = lambda x: x[0])[0]
	min_y = min(data, key = lambda x: x[1])[1]
	max_y = max(data, key = lambda x: x[1])[1]
	return [min_x, max_x, min_y, max_y]

def normalize_data(data):
	new_data = []
	min_x, max_x, min_y, max_y = calculate_min_max(data)
	for x, y in data:
		x = (x - min_x) / (max_x - min_x)
		y = (y - min_y) / (max_y - min_y)
		new_data.append([x, y])
	return new_data

def draw_thetas(ax, theta0, theta1):
	X = ax.get_xbound()
	Y = [theta0 * x + theta1 for x in X]
	ax.plot(X, Y)

def draw_points(ax, X, Y):
	return ax.plot(X, Y, 'bo')

sorted_data = []
normalized_data = []
X = []
Y = []
with open("./data/data.csv", "r") as f:
	f.readline()
	for line in f:
		x, y = line.split(",")
		sorted_data.append([float(x), float(y)])
	sorted_data.sort(key = lambda x: x[0])
	normalized_data = normalize_data(sorted_data)
	for x, y in normalized_data:
		X.append(float(x))
		Y.append(float(y))

if __name__ == "__main__":
	delta_rate = 0.001
	delta_mse = -1
	previous_mse = 0
	theta0, theta1 = calculate_default_thetas(X, Y)

	fig, ax = plt.subplots()
	plt.title("ft_linear_regression")
	plt.xlabel("Kilometrage")
	plt.ylabel("Prix de vente")

	while abs(delta_mse) > 0.000000001:
		previous_mse = calculate_mean_square_error(theta0, theta1, normalized_data)
		gradient = calculate_gradient(normalized_data, theta0, theta1)
		theta0 = theta0 - delta_rate * gradient[0]
		theta1 = theta1 - delta_rate * gradient[1]
		delta_mse = previous_mse - calculate_mean_square_error(theta0, theta1, normalized_data)

	draw_points(ax, X, Y)
	draw_thetas(ax, theta0, theta1)
	plt.show()

