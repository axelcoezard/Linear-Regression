def average(list):
	"""
	Calcul de la moyenne d'une liste
	"""
	return sum(list) / len(list)

def variance(list):
	"""
	Calcul de la variance d'une liste
	"""
	m = average(list)
	return sum([(x - m) ** 2 for x in list]) / len(list)

def covariance(list1, list2):
	"""
	Calcul de la covariance entre deux listes
	"""
	m1 = average(list1)
	m2 = average(list2)
	return sum([(x - m1) * (y - m2) for x, y in zip(list1, list2)]) / len(list1)

X = []
Y = []

with open("./data/data.csv", "r") as f:
	f.readline()
	for line in f:
		x, y = line.split(",")
		X.append(float(x))
		Y.append(float(y))

a = covariance(X, Y) / variance(X)
b = average(Y) - a * average(X)

print(a, "x +", b)
x = input("x = ")
print(a * float(x) + b)
