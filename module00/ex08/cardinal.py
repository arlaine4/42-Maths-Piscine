def get_set_cardinal(s):
    lst_elems = []
    for elem in s:
        if elem not in lst_elems:
            lst_elems.append(elem)
    return len(lst_elems)


def clean_set_before_card(s):
    new_s = []
    float_bool = True
    for elem in s:
        if elem.isnumeric():
            new_s.append(elem)
        elif '.' in elem and elem[0].isnumeric():
            elem = elem.split('.')
            for c in elem:
                if not c.isnumeric():
                    float_bool = False
            if float_bool is True:
                new_s.append(elem)
    return new_s


def cardinal(_set):
    cardinal = 0
    _set = clean_set_before_card(_set)
    print_format = ['n(', 'Ø', ') = ', cardinal]
    if len(_set) == 1 and _set[0] == '':
        print(''.join(map(str, print_format)))
    else:
        print_format[1] = 'S'
        cardinal = get_set_cardinal(_set)
        print_format[-1] = cardinal
        print(''.join(map(str, print_format)))

