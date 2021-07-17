def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
    return result

def format_product(product):
    s = ', '.join(map(str, product))
    s = s.replace('(', '{').replace(')', '}')
    if '{' not in s:
        s = '{' + s + '}'
    return s

def clean_duplicates(_set):
    dico = list(dict.fromkeys(_set))
    return ''.join(map(str, dico))
    

def powerset(_set):
    powerset = []
    _set = _set.replace(' ', '')
    _set = clean_duplicates(_set)
    for i in range(len(_set)):
        powerset.append(format_product(product(range(2), repeat=i)))
    powerset.append(format_product(_set))
    print(' '.join(map(str, powerset)))
