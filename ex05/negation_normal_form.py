operators = ['!', '|', '^', '&', '>', '=']
from copy import deepcopy


def convert_op_to_nnf(ope):
    if ope == '|':
        return '&'
    elif ope == '&' or ope == '>':
        return '|'


def handle_equality_ope(el1, el2):
    bool_el1 = True if el1 is not None else False
    bool_el2 = True if el2 is not None else False
    new_elem = ''
    if bool_el2:
        new_elem += el2
    if bool_el1:
        new_elem += el1
    new_elem += '&'
    if bool_el2:
        new_elem += el2 + '!'
    if bool_el1:
        new_elem += el1 + '!'
    new_elem += '&|'
    return new_elem


def format_new_nnf_elem(ope, el1, el2):
    new_elem = ''
    if ope != '=':
        if el2 is not None:
            new_elem += el2 + '!'
        if el1 is not None:
            new_elem += el1
            if ope != '>':
                new_elem += '!'
        new_elem += convert_op_to_nnf(ope) if ope != '!' else ''
    elif ope == '=':
        new_elem = handle_equality_ope(el1, el2)
    return new_elem


def update_stack(stack, operator):
    new_elem = ''
    elem1 = None
    elem2 = None
    if len(stack[-1]) == 1:
        elem1 = stack.pop()
    if len(stack[-1]) == 1:
        elem2 = stack.pop()
    new_elem = format_new_nnf_elem(operator, elem1, elem2)
    stack.append(new_elem)
    return stack


def parse_rpn(rpn):
    stack = []
    for elem in rpn:
        if elem not in operators:
            stack.append(elem)
        else:
            stack = update_stack(stack, elem)
    nnf = ''.join(map(str, stack))
    print(nnf)

