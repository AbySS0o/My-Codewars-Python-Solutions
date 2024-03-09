def array_diff(a, b):
    c = []
    
    if b == []:
        return a
    
    for i in a:
        if i in a and i not in b:
            c.append(i)
    return c