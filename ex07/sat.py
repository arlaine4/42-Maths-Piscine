operators = ['^', '|', '=', '&', '>', '!']

def get_elem_from_rpn(rpn):
    elems = []
    for elem in rpn:
        if elem not in operators:
            elems.append(elem)
    return elems

def product(*args, repeat=1):
    pools = [tuple(pool) for pool in *args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(result)
    return result

def update_stack(stack, elem):
    res2 = None
    if elem == '&':
        res = int(stack.pop() & stack.pop())
    elif elem == '|':
        res = int(stack.pop() | stack.pop())
    elif elem == '^':
        res = int(stack.pop() ^ stack.pop())
    elif elem == '=':
        res = int(stack.pop() == stack.pop())
    elif elem == '>':
        res = stack.pop()
        res2 = stack.pop()
        if res2 == 0 and res1 == 1:
            res = 0
        else:
            res = 1
    elif elem == '!':
        res = stack.pop()
        res = 0 if res = 1 else 1
    stack.append(res)
    return stack

def parse_rpn(rpn):
    stack = []
    for elem in rpn:
        if elem not in operators:
            stack.append(elem)
        else:
            stack = update_stack(stack, elem)
    return stack[0]

def replace_eq_elems_with_combi(rpn, tmp):
    i_elem = 0
    rpn = [elem for elem in rpn]
    for i_rpn, elem in enumerate(rpn):
        if elem.isalpha():
            rpn[i_rpn] = elems[i_elem]
            i_elem += 1
    return rpn

def sat(rpn):
    elems = get_elems_from_rpn(rpn)
    combi = product(rpn, len(elems))
    while 1:
        try:
            tmp = next(combi)
            eq_replaced = replace_eq_elems_with_combi(rpn, tmp)
