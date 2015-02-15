def apply(l, fun):
    new_l = []
    for el in l:
        new_l.append(fun(el))
    return new_l

apply(elements, lambda x: abs(x))
