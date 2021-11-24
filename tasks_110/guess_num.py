import random
num = random.randint(1000, 9999)
print(num)

def guess_num_game():
    while True:
        try:
            guess_num = int(input('Введите четырехзначеное число: '))
            if len(str(guess_num)) < 4:
                print('Слишком короткое число')
                continue
            elif len(str(guess_num)) > 4:
                print('Слишком длинное число')
                continue
        except ValueError:
            print('Это не число!!!')
            continue
        result = []
        str_guess_num = str(guess_num)
        for digit in str_guess_num:
            if digit in str(num) and str_guess_num.find(str(digit)) == str(num).find(str(digit)):
                result.append('A')
                continue
            elif digit in str(num) and str_guess_num.find(str(digit)) != str(num).find(str(digit)):
                result.append('B')
                continue
        if ('A' * 4) in result:
            print('Вы наконец-то угадали число')
            break
    return result
print(guess_num_game())













