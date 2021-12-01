def check_num():
    while True:
        try:
            num_10 = int(input('Введите число: '))
        except ValueError:
            print('Это не число!!!')
            continue
        if isinstance(num_10, int):
            break
    return num_10

num_10 = check_num()
num_2 = []

def transfer():
    global num_10
    while True:
        if num_10 % 2 == 0:
            num_2.append(0)
            num_10 = num_10 // 2
        elif num_10 % 2 != 0:
            num_2.append(1)
            num_10 //= 2
        if num_10 == 1:
            num_2.append(1)
            num_2_fin = int(''.join(map(str, num_2[::-1])))
            break
    return num_2_fin
print(transfer())
