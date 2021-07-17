from copy import deepcopy

operators = ['^', '|', '=', '&', '>', '!']


def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
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
        res = 0 if res == 1 else 1
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


def build_dico_from_rpn(rpn):
    dico = {}
    for index, elem in enumerate(rpn):
        if elem not in operators:
            if elem not in dico:
                dico[elem] = [index]
            elif elem in dico:
                dico[elem].append(index)
    return dico


def build_list_order_from_dico(dico):
    lst_order = []
    keys = list(dico.keys())
    lst_order = [elem for elem in keys]
    return lst_order


def replace_eq_elems_with_combi(dico, next_combi, rpn, order):
    new_rpn = deepcopy(rpn)
    for i, elem in enumerate(rpn):
        if elem not in operators:
            for index in dico[elem]:
                new_rpn[index] = next_combi[order.index(elem)]
    return new_rpn

    
def sat(rpn):
    dico = build_dico_from_rpn(rpn)
    order = build_list_order_from_dico(dico)
    combi = product(range(2), repeat=len(dico))
    rpn = [elem for elem in rpn]
    sat_eq = False
    while 1:
        try:
            next_combi = next(combi)
            new_eq = replace_eq_elems_with_combi(dico, next_combi, rpn, order)
            res = parse_rpn(new_eq)
            print(res)
            sat_eq = True if res == 1 else False
        except:
            break
    print("#", sat_eq)

