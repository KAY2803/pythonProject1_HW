from dataclasses import dataclass
from typing import Optional
import datetime


@dataclass
class Courts:
    name: str
    place: str


@dataclass
class Cases:
    number: str
    claims: str
    court: Courts
    applicant: str
    defendant: Optional[str] = None
    third_party: Optional[str] = None
    judge: Optional[str] = None
    date_of_court_hearing: Optional[str] = None


if __name__ == '__main__':
    court_1 = Courts('Арбитражный суд г. Санкт-Петербурга и Ленинградской области', 'СПб, ул. Смольного, д.6')
    case_1 = Cases(
        number='А56-71499/2021',
        applicant='ОАО "МЗ "Арсенал',
        defendant='КИО Санкт-Петербурга',
        third_party='Фонд имущества',
        claims='О признании права собственности на здание 27073',
        court=court_1,
        date_of_court_hearing=str(datetime.datetime(2022, 4, 5, 12, 15))
    )

    print(court_1)
    print(case_1)


