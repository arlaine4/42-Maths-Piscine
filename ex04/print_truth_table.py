import eval_formula as evl
from copy import deepcopy

def product(*args, repeat=1):
	# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
	pools = [tuple(pool) for pool in args] * repeat
	result = [[]]
	for pool in pools:
		result = [x+[y] for x in result for y in pool]
	for prod in result:
		yield tuple(prod)
	return result


def	replace_eq_elems_with_combi(rpn, elems):
	i_elem = 0
	rpn = [elem for elem in rpn]
	for i_rpn, elem in enumerate(rpn):
		if elem.isalpha():
			rpn[i_rpn] = elems[i_elem]
			i_elem += 1
	return rpn


def	get_elems_from_rpn(rpn):
	elems = []
	for elem in rpn:
		if elem.isalpha():
			elems.append(elem)
	return elems


def	format_print_lines(combi, res):
	lines = ['' for elem in combi]
	for i, comb in enumerate(combi):
		for c in comb:
			lines[i] += '| ' + str(c) + ' '
		lines[i] += '| ' + str(res[i]) + ' |'
	return lines


def	print_truth_table(elems, combi, res):
	lines_print = format_print_lines(combi, res)
	for elem in elems:
		print('| '+elem+' ',end='')
	print('|   |')
	print(('|---' * (len(elems) + 1))+'|')
	for line in lines_print:
		print(line)


def	get_truth_table(rpn):
	elems = get_elems_from_rpn(rpn)
	combi = product(range(2), repeat=len(elems))
	res = []
	lst_comb = []
	while 1:
		try:
			tmp = next(combi)
			lst_comb.append(deepcopy(tmp))
			eq_replaced = replace_eq_elems_with_combi(rpn, tmp)
			res.append(evl.parse_rpn(eq_replaced))
		except:
			break
	while 1:
		try:
			lst_comb.append(next(combi_cpy))
		except:
			break
	print_truth_table(elems, lst_comb, res)
