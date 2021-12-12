def first_last(letter, st):
    list_ = []
    for count, value in enumerate(st):
        if letter in value:
            list_.append(count)
    if list_:
        return min(list_), max(list_)
    else:
        return None, None

letter = 'b'
st = 'brave heart beat b'
print(first_last(letter, st))
