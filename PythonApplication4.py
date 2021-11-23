class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer (Mentor):
    pass

class Reviewer (Mentor):
    pass

cool_lectures = Lecturer ('Billy', 'Djin')

cool_reviewer = Reviewer ('Billy', 'Herrington')


print (f'Имя Лектора: {cool_lectures.name}')
print (f'Фамилия Лектора: {cool_lectures.surname}')
print ()
print (f'Имя Рецензента: {cool_reviewer.name}')
print (f'Фамилия Рецензента: {cool_reviewer.surname}')