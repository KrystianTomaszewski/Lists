def in_list(list, n):
    new_list = [x for x in range(1, n+1) if x not in list]
    return new_list


print(in_list([2, 3, 7, 4, 9], 10))