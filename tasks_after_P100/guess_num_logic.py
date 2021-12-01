def check_value():
    while True:
        try:
            guess_num = int(input('Введите четырехзначеное число: '))
        except ValueError:
            print('Это не число!!!')
            continue
        if len(str(guess_num)) < 4:
            print('Слишком короткое число')
            continue
        elif len(str(guess_num)) > 4:
            print('Слишком длинное число')
            continue
        if len(str(guess_num)) == 4:
            break
    return guess_num


