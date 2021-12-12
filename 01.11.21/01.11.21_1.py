lst = [1, 2, 5, 7, 8]
EL = lst[0]

def change(lst):
    lst[0] = lst[-1]
    lst[-1] = EL

    return lst

print(change(lst))


