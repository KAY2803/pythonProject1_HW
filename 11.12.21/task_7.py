# функция, которая создает тестового пользователя

import random
import string
from datetime import date, time, datetime
import json

from mimesis import Person
from mimesis.enums import Gender
from mimesis.locales import Locale


def generate_person(keys: str):
    person = Person(Locale.RU)
    fullname = person.full_name(gender=None)
    population = f'{string.ascii_letters}{string.digits}'
    name_mail = str(''.join(random.sample(population, random.randint(1, 10))))
    domain = ['mail', 'list', 'yandex', 'bk', 'inbox']
    gen_person = {}
    gen_person = {
                      'name': fullname.split()[0],
                      'surname': fullname.split()[1],
                      'login': str(''.join(random.sample(population, random.randint(6, 10)))),
                      'password': str(''.join(random.sample(string.printable, random.randint(6, 10)))),
                      'tel': f'+7{random.randrange(0000000000, 9999999999)}',
                      'mail': f'{name_mail}@{random.choice(domain)}.ru',
                      'register_time': f'{datetime.today()}'
    }
    keys = keys.split()
    final_gen_person = dict.fromkeys(keys)
    for key, value in final_gen_person.items():
        final_gen_person[key] = gen_person[key]
    yield final_gen_person


with open('person', 'w', encoding='utf-8') as file:
    for _ in range(3):
        person = next(generate_person('name mail login'))
        json.dump(person, file, ensure_ascii=False, indent=4)





