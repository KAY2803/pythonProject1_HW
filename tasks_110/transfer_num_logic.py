def check_num():
    while True:
        try:
            num_10 = int(input('Введите число: '))
        except ValueError:
            print('Это не число!!!')
            continue
        if isinstance(num_10, int):
            break