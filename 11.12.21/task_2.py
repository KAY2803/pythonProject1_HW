#Task 2
#Скрипт имитирующий зрительскую волну для строки.
#Строка ввода всегда будет в нижнем регистре, но может быть пустой.
#Если символ в строке является пробелом, пропустите его.

# example
#wave("hello") =>
#"Hello"
#"hEllo"
#"heLlo"
#"helLo"
#"hellO"

def wave(str_):
    str_ = str_.lower()
    for i in range(len(str_)):
        if str_[i].isalpha():
            str2 = str_[:i] + str_[i].upper() + str_[i+1:]
            print(str2)


wave("Hello, world!")


word = 'Hello'
lst = []
if __name__ == "__main__":
    for index, element in enumerate(word):
        if element == " ":
            continue
        if element.isalpha():
            a = word[:index]
            b = word[index + 1:]
            lst.append("".join((a, element.upper(), b)))
            print("lst", lst)