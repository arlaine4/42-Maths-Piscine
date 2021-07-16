operators = ['!', '|', '^', '&', '>', '=']
tmp = ''
from copy import deepcopy

"""
The goal here is to build an AST(abstract syntax tree) from a rpn(reverse
polish notation) formula.

ex: 101|& ->      &
                /   \
              |       1   -> wich evaluates to be True
            /  \
           0    1
"""

class Node:
    """
    The node class represents the entire ast
    inside l(left) and r(right) attributes we other Node instances
    with other l and r elems.
    """
    def	__init__(self, elem_val, l=None, r=None, bool_neg=False):
            self.elem = elem_val
            self.l = l
            self.r = r
            self.res = None

    def	get_res(self):
            """
            assign result to a node instance, either the base node,
            or let's say node.l or node.r, it can even be node.l.l.
            The tmp variable helps to know if we need to invert the
            result we are getting
            """
            global tmp
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
            elif tmp == '!':
                    self.res = True if self.res is False else False
            self.res = True if self.res == 1 else False

    def	__str__(self):
            if self.l is not None and self.r is not None:
                    return '{0} -> left : {1}\n{0} -> right : {2}'.format(self.elem, self.l.elem, self.r.elem)
            elif self.l is not None and self.r is None:
                    return '{} -> left : {}'.format(self.elem, self.l.elem)
            elif self.l is None and self.r is not None:
                    return '{} -> right : {}'.format(self.elem, self.r.elem)
            else:
                return '{0} -> left : Ast end\n{0} -> right : Ast end'.format(self.elem)

def build_node(stack):
    """
    Building first node instance from the stack elems,
    We instanciate other node instances inside node.l and node.r
    if we have enough elems inside the stack
    """
    node_inst = Node(stack[0])
    if len(stack) >= 2:
            node_inst.l = Node(stack[1])
            if len(stack) >= 3 and stack[0] != '!':
                    node_inst.r = Node(stack[2])
    return node_inst

def update_stack(stack):
    if len(stack) >= 2:
            if stack[1] and stack[1] not in operators:
                    stack.pop(1)
    if len(stack) >= 2:
            if stack[1] and stack[1] not in operators:
                    stack.pop(1)
    return stack

def print_node(node):
    """
    Recursion call to Node.__str__() with firstly
    the base node level, so node.elem, node.l.elem and node.r.elem,
    and then if we have left and/or right Node(s) we call print_node
    again with node.left or node.right
    """
    print(node)
    if node.l is not None:
        return print_node(node.l)
    if node.r is not None:
        return print_node(node.r)

def build_new_root(elem, node, stack):
    """
    Similar to build_node() but here we want to create a new root
    node from existing ones, we just add one on top of the graph
    by assigning node_inst.l with previous node
    """
    node_inst = Node(elem)
    if elem == '!' and len(stack) >= 1:
            node_inst.l = node
    elif len(stack) >= 2:
            node_inst.l = node
            if len(stack) >= 2 and stack[0] != '!':
                    node_inst.r = Node(stack[-1])
    return node_inst

def parse_rpn(rpn):
    """
    Parsing rpn, we use a stack to pop and append elems
    in order to build the abstract syntax tree
    """
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
                node = new_node
                stack = update_stack(stack)
        else:
            stack.append(elem)
    eval_node(node)

def eval_node(node):
    """
    Evaluation of the abstract syntax tree, the global tmp
    helps us with keeping in mind if we are doing a recursion with a !
    operator
    """
    global tmp
    if node.elem in operators and node.elem != '!':
        if node.l.elem in operators:
            return eval_node(node.l)
        if node.r.elem in operators:
            return eval_node(node.r)
    if node.elem != '!' and node.l.elem not in operators and node.r.elem not in operators:
        node.get_res()
        node.elem = node.res
    if node.elem == '!':
        tmp = '!'
        return eval_node(node.l)
    if tmp == '!':
        node.get_res()
        node.elem = node.res
        tmp = ''
    res = str(node.elem)
    print('#', res.lower())

