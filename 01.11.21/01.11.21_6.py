def count_it(sequence):
    from collections import Counter
    dict_ = {}
    for number in sequence:
        dict_ = Counter(sequence).most_common(3)
    return dict(dict_)

sequence = '0855876450875096072465143784013254'
print(count_it(sequence))