# Написать генератор, возвращающий по 3 символа из текстового файла, при этом не загружая в память весь файл.

def gen_return(n: int):
    with open('output.txt', 'r', encoding='utf8') as file:
        for symbol in file.read():
            yield symbol[:n]

symbols = gen_return(5)
for _ in range(15):
    print(next(symbols), end='')
