def	adder(nb1, nb2):
	nb1, nb2 = int(nb1), int(nb2)
	while nb2 != 0:
		tmp = nb1 & nb2
		nb1 = nb1 ^ nb2
		nb2 = tmp << 1
	return nb1

