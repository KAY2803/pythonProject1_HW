# Написать генератор, возвращающий по одному слову текстового файла, при этом не загружая в память весь файл
# В качестве разделителя слов использовать символ пробела

def gen_return():
    with open('output.txt', 'r') as file:
        for word in file.read().split(' '):
            yield word

words = gen_return()
for _ in range(4):
    print(next(words), end=' ')