def set_eq(set1, set2):
    set1_elems, set2_elems = [], []
    for elem in set1:
        if elem not in set1_elems:
            set1_elems.append(elem)
    for elem in set2:
        if elem not in set1_elems:
            return False
        if elem not in set2_elems:
            set2_elems.append(elem)
    for elem in set1_elems:
        if elem not in set2_elems:
            return False
    return True
