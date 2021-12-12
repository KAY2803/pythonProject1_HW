#message = ''
#toppings = ['cheese', 'mushrooms', 'pepper']

#while message != 'quit':
 #   message = input("Выберете топпинг для пиццы: ")
 #   toppings.append(message)
 #   if message == 'quit':
 #       print("Мы начали делать Вашу пиццу")
 #   else:
 #       print(f"{message.title()} включен в заказ")

def make_album():
    album = {}
    while True:
        key = str(input("Введите исполнителя (введите 'q', если хотите завершить): "))
        value = str(input("Введите название альбома (введите 'q', если хотите завершить): "))
        for key, value in album:
            if key != 'q' or value != 'q':
                album[key] = value
        if key == 'q' or value == 'q':
            break

    return album

print(make_album())