
if __name__ == "__main__":
	theta0 = 0
	theta1 = 0

	with open("./data/thetas.csv", "r") as f:
		f.readline()
		theta0, theta1 = f.readline().split(",")
		theta0 = float(theta0)
		theta1 = float(theta1)
		f.close()

	value = float(input("Nombre de kilometres au compteur de la voiture:\n"))
	print("=> La voiture devrait pouvoir se vendre", round(theta0 * value + theta1, 2), "euros.")
