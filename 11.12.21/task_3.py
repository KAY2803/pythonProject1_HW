# генератор бесконечной волны, который будет "гонять" строку влево и вправо пока будет происходить вызов генератора.
# Можно сделать не со строкой, а с символами, где текущий знак будет заменяться на другой символ

## example 1     example 2
"Hello"         "*---"
"hEllo"         "-*--"
"heLlo"         "--*-"
"helLo"         "---*"
"hellO"         "--*-"
"helLo"         "-*--"
"heLlo"         "*---"
"hEllo"
"Hello"

# example 1
def endless_gen(word: str):
    word = word.lower()
    one_way = range(len(word))
    while True:
        for i in one_way:
            new_word = word[:i] + word[i].upper() + word[i + 1:]
            yield new_word
            if i == len(word)-2:
                one_way = reversed(list(range(1, len(word)-1)))
                i -= 1
            if i == 1:
                one_way = range(len(word))


mygen = endless_gen('mmmmm')
for _ in range(10):
    print(next(mygen))

# example 2
def endless_gen(line: str):
    one_way = range(len(line))
    while True:
        for i in one_way:
            new_line = line[:i] + '*' + line[i + 1:]
            yield new_line
            if i == len(line)-2:
                one_way = reversed(list(range(1, len(line)-1)))
                i -= 1
            if i == 1:
                one_way = range(len(line))


mygen = endless_gen('-----')
for _ in range(10):
    print(next(mygen))
