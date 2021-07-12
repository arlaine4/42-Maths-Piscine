def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


if __name__ == "__main__":
#	lst = [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
#	lst = [0, 0, 0, 1, 0, 1, 1, 1, 1]
#	res = combinations_with_replacement(lst, 5)
#	res = combinations_with_replacement(lst, 4)
	lst = [0, 0, 0, 1, 1, 1]
	res = combinations_with_replacement(lst, 3)
	while 1:
		try:
			print(next(res))
		except:
			break
	print()
	lst = [1, 1, 0, 1, 0, 0]
	res = combinations_with_replacement(lst, 3)
	while 1:
		print(next(res))
