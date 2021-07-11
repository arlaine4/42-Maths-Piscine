operators = ['!', '|', '^', '&', '>', '=']
from copy import deepcopy


class Node:
	def	__init__(self, elem_val, l=None, r=None):
		self.elem = elem_val
		self.l = l
		self.r = r
		self.res = None

	def	get_res(self):
		if self.elem == '|':
			self.res = int(self.l.elem) | int(self.r.elem)
		elif self.elem == '&':
			self.res = int(self.l.elem) & int(self.r.elem)
		elif self.elem == '^':
			self.res = int(self.l.elem) ^ int(self.r.elem)
		elif self.elem  == '=':
			self.res = int(self.l.elem) == int(self.r.elem)
		elif self.elem == '>':
			self.res = int(self.l.elem) == int(self.r.elem)
		elif self.elem == '!':
			if self.l is None:
				self.res = int(self.r.elem) * -1
			elif self.r is None:
				self.res = int(self.l.elem) * -1
		self.res = True if self.res == 1 else False

	def	__str__(self):
		return '{0}->left : {1}\n{0}->right : {2}\t {1} res : {3}'.format(self.elem, self.l, self.r, self.res)
#		return '{}->left : {}\n{}->right : {}'.format(self.elem, self.l, self.elem, self.r)

def	build_node(stack):
	node_inst = Node(stack[0])
	if len(stack) >= 2:
		node_inst.l = Node(stack[1])
		if len(stack) >= 3:
			node_inst.r = Node(stack[2])
	return node_inst

def	update_stack(stack):
	if len(stack) >= 2:
		if stack[1] and stack[1] not in operators:
			stack.pop(1)
	if len(stack) >= 2:
		if stack[1] and stack[1] not in operators:
			stack.pop(1)
	return stack

def	build_new_root(elem, node, stack):
	node_inst = Node(elem)
	if len(stack) >= 2:
		node_inst.l = node
		if len(stack) >= 2:
			node_inst.r = Node(stack[-1])
	return node_inst

def	parse_rpn(rpn):
	stack = []
	node = None
	for elem in rpn:
		if elem in operators:
			if node is None:
				stack.insert(0, elem)
				node = build_node(stack)
				stack = update_stack(stack)
			else:
				stack.insert(0, elem)
				new_node = build_new_root(elem, node, stack)
				node = deepcopy(new_node)
				stack = update_stack(stack)
		else:
			stack.append(elem)
	eval_node(node)


def	eval_node(node):
	if node.elem in operators:
		if node.l.elem in operators:
			return eval_node(node.l)
		if node.r.elem in operators:
			return eval_node(node.r)
		if node.l.elem not in operators and node.r.elem in operators:
			return eval_node(node.r)
		if node.r.elem not in operators and node.l.elem in operators:
			return eval_node(node.l)
		elif node.l.elem not in operators and node.l.elem not in operators:
			node.get_res()
			node.elem = node.res
	res = str(node.elem)
	print("#", res.lower())
