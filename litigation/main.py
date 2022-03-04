from typing import Optional

import datetime
import json

from cases import Courts, Cases
from staff import Employee


class Litigation:

    def __init__(self,
                 case: Cases,
                 team: Optional[Employee] = None):
        self.case = case
        self.team = team
        # self.automatic_tasks

    def _save(self):
        pass # json

    def _add_team(self, members: [Employee, ...]):
        if self.team is None:
            self.team = members
        else:
            self.team.append(members)
        return self.team

    def __repr__(self):
        return f'дело: {self.case}, сотрудники проекта: {self.team}'


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
    e_1 = Employee('Ким А.Ю.', 'советник')
    e_2 = Employee('Селевцова К.К.', 'юрист')
    e_3 = Employee('Будкина И.В.', 'юрист')
    lit_1 = Litigation(case_1, e_1)
    case_1.judge = 'Н.Е. Целищева'
    lit_1.team + e_1
    # lit_1._add_team([e_3])

    print(lit_1)
