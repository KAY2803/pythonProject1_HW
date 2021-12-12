def search_substr(subst, st):

    if subst.lower() in st.lower():
        return "Есть контакт"
    else:
        return "Мимо"

subst = "весь день"
st = "Сегодня весь день светит солнце"
print(search_substr(subst, st))