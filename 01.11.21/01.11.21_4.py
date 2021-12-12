def all_eq(str_1, str_2):

    new_list = []
    lenght = max(len(str_1), len(str_2))
    new_list.append((str_1).ljust(lenght, "_"))
    new_list.append((str_2).ljust(lenght, "_"))
    return new_list

str_1 = "Мороз и солнце день чудесный"
str_2 = "еще ты дремлешь"
print(all_eq(str_1, str_2))