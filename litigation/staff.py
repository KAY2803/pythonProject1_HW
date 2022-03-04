from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    position: str


class Team (Employee):

    def __init__(self, team: [Employee, ...]):
        self.team = team

    def _add_team(self, members: [Employee, ...]):
        if self.team is None:
            self.team = members
        else:
            self.team.append(members)
        return self.team

    def __repr__(self):
        return f'команда проекта: {self.team}'

if __name__ == '__main__':
    e_1 = Employee(name='Ким А.Ю.', position='советник')
    e_2 = Employee(name='Селевцова К.К.', position='юрист')
    e_3 = Employee(name='Будкина И.В.', position='юрист')
    team_1 = Team([e_1])
    team_1._add_team([e_2, e_3])


    print(e_1, e_2, e_3)
    print(team_1)