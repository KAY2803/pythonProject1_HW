def check_Luna_original():
    check_num = list(input('Введите проверочное число '))
    check_sum = sum(map(int, check_num[-1::-2]))
    for x in check_num[-2::-2]:
        x = int(x) * 2
        if x <= 9:
            check_sum += x
        else:
            mod_x = sum(map(int, str(x)))
            check_sum += mod_x
    if check_sum % 10 == 0:
        return check_sum, 'Исходные данные верны'
    else:
        return check_sum, 'В исходных данных ошибка'
print(check_Luna_original())
