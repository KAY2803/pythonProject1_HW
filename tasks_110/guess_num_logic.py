import random
import string

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
print(check_value())

def check_result():
    num = random.randint(1000, 9999)
    guess_num = int(input('Введите четырехзначеное число: '))
    result = []
    str_guess_num = str(guess_num)
    for digit in str_guess_num:
        if digit in str(num) and str_guess_num.find(str(digit)) == str(num).find(str(digit)):
            result.append('A')
        elif digit in str(num) and str_guess_num.find(str(digit)) != str(num).find(str(digit)):
            result.append('B')
        else:
            pass
    return result


