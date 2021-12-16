# функция, которая принимает римское число в качестве аргумента и возвращает его значение
# как числовое десятичное целое число.


def roman_to_int(roman_num: str):
    roman_num = list(roman_num.upper())
    num_list = []
    converter = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
    for r_num in roman_num:
        r_num = int(converter.get(r_num))
        num_list.append(r_num)
    arabic_num = 0
    index = 0
    while True:
        # проверяем, являются ли первые числа тысячами
        if num_list[index] == 1000:
            if num_list[index] == num_list[index + 1]:
                arabic_num += (num_list[index] + num_list[index + 1])
                index += 2
            elif num_list[index] == num_list[index + 1] == num_list[index + 2]:
                arabic_num += (num_list[index] + num_list[index + 1] + num_list[index + 2])
                index += 3
            else:
                arabic_num += num_list[index]
                index += 1
        else:
            # проверяем является ли число последним в списке
            if index == len(num_list) - 1:
                arabic_num += num_list[index]
                index += 1
            else:
                if num_list[index] == num_list[index + 1]:
                    arabic_num += (num_list[index] + num_list[index + 1])
                    index += 2
                elif num_list[index] < num_list[index + 1]:
                    arabic_num += (num_list[index+1] - num_list[index])
                    index += 2
                elif num_list[index] > num_list[index + 1]:
                    arabic_num += (num_list[index+1] + num_list[index])
                    index += 2
                else:
                    arabic_num += num_list[index]
        if index == len(num_list):
            break
    return arabic_num


print(roman_to_int('XlIX'))
