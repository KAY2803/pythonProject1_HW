from dataclasses import dataclass
from staff import Employee
import datetime


@dataclass
class AutomaticTasks:
    name: str
    doer: Employee
    responsible: Employee
    duration: str


if __name__ == '__main__':

    e_3 = Employee('Будкина И.В.', 'юрист')
    at_1 = AutomaticTasks(
        name='Ознакомиться с материалами дела',
        doer=e_3,
        responsible=e_3,
        duration=str(datetime.date.today() + datetime.timedelta(days=1))
    )

    print(at_1)


