# Написать генератор, возвращающий  последние n строк из текстового файла, при этом не загружая в память весь файл

def gen_return():
    with open('output.txt', 'r') as file:
        for line in file.readlines()[::-1]:
            yield line.strip()

lines = gen_return()
for _ in range(4):
    print(next(lines))