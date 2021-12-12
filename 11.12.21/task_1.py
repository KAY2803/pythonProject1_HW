#Task 1
#Скрипт для конвертации списка с 1 и 0, в целочисленное значение.

#Списки могут иметь разную длину.

# example
#[0, 1, 1, 0] ==> 6
#[1, 1, 1, 1] ==> 15

num_2 = list(input('Введите цифры 1 и/или 0: '))
pow_ = len(num_2) - 1
num_10 = 0
for num in num_2:
    num_1 = int(num) * (2 ** pow_)
    pow_ -= 1
    num_10 += num_1
print(num_10)

list_1 = [0, 1, 1, 0, 1]
str_ = "".join(map(str, list_1))
dec_ = int(str_, 2)
print(dec_)