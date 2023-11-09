def friend(x):
    my_friends = []
    for i in x:
        if len(i) == 4:
            my_friends.append(i)
    return my_friends