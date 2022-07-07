
if __name__ == "__main__":
	theta0 = 0
	theta1 = 0

	with open("./data/thetas.csv", "r") as f:
		f.readline()
		theta0, theta1 = f.readline().split(",")
		theta0 = float(theta0)
		theta1 = float(theta1)
		f.close()

	print("theta0:", theta0)
	print("theta1:", theta1)
	value = float(input("input value: "))
	print("value:", theta0 * value + theta1)
