# Написать декоратор, сохраняющий результат в файл output.txt помимо возвращения.
# Результаты должны накапливаться в файле.

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        with open('output.txt', 'a') as file:
            for item in result:
                file.write(str(item))
                file.write('\n')
        return result

    return wrapper

@decorator
def return_func(*args):
    return args


print(return_func(1, 2, 3))
print(return_func(['Hello, world']))