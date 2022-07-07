def print_header():
	print("""\033[1;32m█████████  █████                        █████
  ███░░░░░███░░███                        ░░███
 ███     ░░░  ░███████    ██████   ██████  ░███ █████  ██████  ████████
░███          ░███░░███  ███░░███ ███░░███ ░███░░███  ███░░███░░███░░███
░███          ░███ ░███ ░███████ ░███ ░░░  ░██████░  ░███████  ░███ ░░░
░░███     ███ ░███ ░███ ░███░░░  ░███  ███ ░███░░███ ░███░░░   ░███
 ░░█████████  ████ █████░░██████ ░░██████  ████ █████░░██████  █████
  ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░\033[0m""")

def load_thetas():
	theta0 = 0
	theta1 = 0

	with open("./data/thetas.csv", "r") as f:
		f.readline()
		theta0, theta1 = f.readline().split(",")
		theta0 = float(theta0)
		theta1 = float(theta1)
		f.close()

	return theta0, theta1

def load_data():
	X = []
	Y = []
	with open("./data/data.csv", "r") as f:
		f.readline()
		for line in f:
			x, y = line.split(",")
			X.append(int(x))
			Y.append(int(y))
		f.close()
	return X, Y

if __name__ == "__main__":
	print_header()

	theta0, theta1 = load_thetas()
	X, Y = load_data()

	total_error = 0
	for index, x in enumerate(X):
		y1 = Y[index]
		y2 = theta0 * x + theta1
		error = abs(y1 - y2) * 100 / y1
		print(str(index).ljust(3), "Δ(" + str(x).rjust(6) + ") =", str(round(error, 2)).rjust(5), "%")
		total_error += error
	avg_error = total_error / len(X)
	print("\nMoyenne de l'erreur:", str(round(avg_error, 2)).rjust(5), "%")

