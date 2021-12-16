# функция, которая текущее время конвертирует в формат заданный пользователем
# time_from_pattern(time.time(), "YYYY-mm-dd") => "2021-12-22"
import re
import time
import string

def time_from_pattern(f_date:str):
    t = time.time()
    format_t = '-'.join(map(str, time.localtime(t)))
    date_pattern = re.search(r'(?P<year>\b\d{4}\b)-(?P<month>\b\d{2}\b)-(?P<day>\b\d{2}\b)', format_t)
    format_date = date_pattern.group(1, 2, 3)
    delimetr_pattern = re.search(r'[a-zA-Z]+(?P<delimetr>[\W+|_+|\s+])[a-zA-Z]+', f_date)
    delimetr = delimetr_pattern.group(1)
    date = re.split('[-|,|:|;|\.|_|/]', f_date.lower())
    for index, name in enumerate(date):
        if 'y' in name:
            date[index] = format_date[0]
        elif 'm' in name:
            date[index] = format_date[1]
        elif 'd' in name:
            date[index] = format_date[2]
    final_date = delimetr.join(date)
    # другой вариант
    # final_date = f'{format_date[0]}-{format_date[1]}-{format_date[2]}'

    time_ = time.strftime('%H:%M:%S', time.localtime(t))
    return final_date, time_


date_time = time_from_pattern("YYYY/mm/dd")
print(f'date: {date_time[0]}')
print(f'time: {date_time[1]}')
