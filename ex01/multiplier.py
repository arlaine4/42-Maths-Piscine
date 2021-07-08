from adder import adder

def	multiplier(nb1, nb2):
	result = 0
	loop_count = 0
	while nb2 != 0:
		if nb2 % 2 == 1:
			tmp_result = nb1 << loop_count
			result = adder(result, tmp_result)
		loop_count += 1
		nb2 >>= 1
	return result

