import random
import guess_num_logic
num = random.randint(1000, 9999)
print(num)

def guess_num_game():
    while True:
        str_guess_num = str(guess_num_logic.check_value())
        result = []
        for digit in str_guess_num:
            if digit in str(num) and str_guess_num.find(str(digit)) == str(num).find(str(digit)):
                result.append('A')
            elif digit in str(num) and str_guess_num.find(str(digit)) != str(num).find(str(digit)):
                result.append('B')
            else:
                continue
        if str_guess_num != str(num):
            print(f'{result}\nПродолжаем')
            continue
        elif str_guess_num == str(num):
            print('Поздравляю! Вы угадали число!')
            break
    return result
print(guess_num_game())













