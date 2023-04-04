groupmates = [
    {
        'name': 'Ivan',
        'surname': 'Ivanov',
        'exams': ['Informatics', 'EEiS', 'Web'],
        'marks': [4, 3, 5]
    },
    {
        'name': 'Artem',
        'surname': 'Sidorov',
        'exams': ['History', 'AiG', 'TTP'],
        'marks': [4, 4, 4]
    },
    {
        'name': 'Veniamin',
        'surname': 'Skobelev',
        'exams': ['Philosophic', 'IS', 'KTP'],
        'marks': [5, 3, 4]
    },
    {
        'name': 'Kirill',
        'surname': 'Tigrov',
        'exams': ['Mathematica', 'physics', 'Web'],
        'marks': [3, 5, 5]
    },
    {
        'name': 'Denis',
        'surname': 'Uvarov',
        'exams': ['Literature', 'THP', 'Web'],
        'marks': [4, 3, 5]
    },
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


print_students(groupmates)
