
def fn(word):
    center = int(len(word)/2)
    if len(word) % 2 == 0:
        word_1 = ''.join(reversed(word[0:center]))
        word_2 = ''.join(reversed(word[center:]))
        print(word_1 + word_2)
    else:
        word_1 = ''.join(reversed(word[0:center]))
        word_2 = ''.join(reversed(word[center+1:]))
        print(word_1 + word[center] + word_2)

print(fn('example'))