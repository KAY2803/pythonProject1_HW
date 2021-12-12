def rus_alphabet():
    alphabet_start = ord('а')
    dict_rus_alpha = {}
    rus_slphabet = ''.join([chr(i) for i in range(alphabet_start, alphabet_start + 32)])
    for weight, char in enumerate(rus_slphabet, 1):
        dict_rus_alpha.update({char: weight})
    return dict_rus_alpha

def get_word_with_max_weigt(input_string):
    weight_word_list = []
    alphabet_rus = rus_alphabet()
    word_list = input_string.split()
    for word in word_list:
        word_weight = 0
        for char in word:
            word_weight += alphabet_rus.get(char, 0)
        weight_word_list.append(word_weight)
    return word_list[weight_word_list.index(max(weight_word_list))]

str_ = 'мама мыла раму'
print(get_word_with_max_weigt(str_))
