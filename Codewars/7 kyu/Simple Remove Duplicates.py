def solve(arr): 
    new_list = []
    for i in arr[::-1]:
        if i not in new_list:
            new_list.append(i)
    return new_list[::-1]