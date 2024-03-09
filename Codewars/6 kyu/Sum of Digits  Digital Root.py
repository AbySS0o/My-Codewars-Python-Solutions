def digital_root(n):
    while len(str(n)) != 1:
        num = [int(i) for i in str(n)]
        n = sum(num)
        
    return n