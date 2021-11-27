# Написать генератор, возвращающий по 3 символа из текстового файла, при этом не загружая в память весь файл.

def gen_return(n: int):
    with open('output.txt', 'r') as file:
        for _ in range(100):
            yield file.read(n)

symbols = gen_return(3)
for _ in range(4):
    print(next(symbols))