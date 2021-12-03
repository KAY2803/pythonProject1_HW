# Написать генератор, возвращающий по 3 символа из текстового файла, при этом не загружая в память весь файл.

def gen_return(n: int):
    with open('output.txt', 'r', encoding='utf8') as file:
        for str_ in file.read():
            yield str_[:3]

symbols = gen_return(3)
for _ in range(12):
    print(next(symbols), end='')
