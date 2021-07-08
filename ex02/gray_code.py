def	gray_code(nb):
	"""
	About the solving method:
	We get the result with the exclusive OR method between
	the base number and the same binary shifted right one time,
	there is other methods but that's the one I used
	
	let's take an example with 7:
	  0111 -> base number
	^ 0011 -> same number shifted to the right once
	-------
	  0100 -> result in binary that will just be converted
			  by the python interpreter when printing the
			  result
	"""
	shifted_nb = nb >> 1
	return nb ^ shifted_nb
