#list_message = ['привет', 'how are you?', "what's the matter"]
#def print_message(list_message):
 #   sent_mes = []
 #   while list_message:
 #       print(list_message[-1])
 #       sent_mes.append(list_message.pop())

 #   return sent_mes

#print(print_message(list_message))

def info_auto(manufactor, model, **dict_auto):
    dict_auto['manufactor'] = manufactor
    dict_auto['model'] = model

    return dict_auto

for key, value in info_auto('mers', 'A35', color='white', comp='AMG').items():
    print(key, value)
