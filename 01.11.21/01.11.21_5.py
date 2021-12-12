def to_dict(lst):
    dict = {}
    for element in lst:
        dict[element] = element
    return dict

lst = [1, 'nhblfnm', 986, 'uyshv']
print(to_dict(lst))