import transfer_num_logic

def transfer_num_10_to_2():
    transfer_num_logic.check_num()
    num_2 = []
    while True:
        if num_10 % 2 == 0:
            num_2.append(0)
            num_10 = num_10 // 2
        elif num_10 % 2 != 0:
            num_2.append(1)
            num_10 = num_10 // 2
        if num_10 == 1:
            num_2.append(1)
            num_2_fin = int(''.join(map(str, num_2[::-1])))
            break
    return num_2_fin
print(transfer_num_10_to_2())




