def more_than_five(lst):
    new_lst = [number for number in lst if number not in range(-5, 6)]
    return new_lst

lst = [4, 6, 87, 88, -3, -54, 0]
print(more_than_five(lst))