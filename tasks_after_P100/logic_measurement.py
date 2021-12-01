def transfer_temperature():
    celsiy = 0
    farengeit = 0
    while True:
        input_system = str.upper(input('Выберете параметры ввода: C или F '))
        if input_system != 'C' and input_system != 'F':
            print('только C или F (латинские)')
            continue
        try:
            input_temperature = float(input('Введите данные по температуре '))
        except ValueError:
            print('Можно ввести только целое число или число с точкой ')
            continue
        if input_system == 'C':
            farengeit = (input_temperature * 9 / 5) + 32
        elif input_system == 'F':
            celsiy = (input_temperature - 32) * 5 / 9
        return celsiy if input_system == 'F' else farengeit

def transfer_km_miles():
    miles = 0
    kilometres = 0
    while True:
        input_system = str.upper(input('Выберете параметры ввода: M или K '))
        if input_system != 'M' and input_system != 'K':
            print('только M или K (латинские)')
            continue
        try:
            input_distance = float(input('Введите данные по расстоянию '))
        except ValueError:
            print('Можно ввести только целое число или число с точкой ')
            continue
        if input_system == 'M':
            kilometres = input_distance * 1.60934
        elif input_system == 'K':
            miles = input_distance * 0.621371
        return miles if input_system == 'K' else kilometres

def transfer_weight():
    ounce = 0
    gram = 0
    while True:
        input_system = str.upper(input('Выберете параметры ввода: O или G '))
        if input_system != 'O' and input_system != 'G':
            print('только O или G (латинские)')
            continue
        try:
            input_weight = float(input('Введите данные по весу '))
        except ValueError:
            print('Можно ввести только целое число или число с точкой ')
            continue
        if input_system == 'O':
            gram = input_weight * 28.3495
        elif input_system == 'G':
            ounce = input_weight * 0.035274
        return gram if input_system == 'O' else ounce

