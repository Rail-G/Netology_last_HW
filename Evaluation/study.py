class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
         
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._div}\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {(", ".join(self.finished_courses) if len(self.finished_courses) > 0 else "Нету")}'
    
    @ property
    def _div(self):
        s_n = 0
        s_l = 0
        for i_k, i_v in self.grades.items():
            r = sum(i_v)  
            s_l += len(i_v)
            s_n += r
        if s_l == 0:
            return "У студента нету оценок"
        return s_n / s_l
    
    def __gt__(self, other):
        if isinstance(other, Student):
            if self._div == "У студента нету оценок" or other._div == "У студента нету оценок":
                return 'Упс... Этот студент еще не учиться, поэтому не имеет оценок'
            return float(self._div) > float(other._div)

    
    def __lt__(self, other):
        if isinstance(other, Student):
            if self._div == "У студента нету оценок" or other._div == "У студента нету оценок":
                return 'Упс... Этот студент еще не учиться, поэтому не имеет оценок'
            return float(self._div) < float(other._div)
            
        
    def __eq__(self, other):
        if isinstance(other, Student):
            if self._div == "У студента нету оценок" or other._div == "У студента нету оценок":
                return 'Упс... Этот студент еще не учиться, поэтому не имеет оценок'
            return self._div == other._div
    
    def __ne__(self, other):
        if isinstance(other, Student):
            if self._div == "У студента нету оценок" or other._div == "У студента нету оценок":
                return 'Упс... Этот студент еще не учиться, поэтому не имеет оценок'
            return self._div != other._div


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__ (self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self._div}'

    @ property
    def _div(self):
        s_n = 0
        s_l = 0
        for i_k, i_v in self.grades.items():
            r = sum(i_v) 
            s_l += len(i_v)
            s_n += r
        if s_l == 0:
            return 'У лектора нету оценок'
        return f'{s_n / s_l:.2f}'
    
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            if self._div == 'У лектора нету оценок' or other._div == 'У лектора нету оценок':
                return 'Упс... Лектор не имеет оценки, он не поулярен :('
        return self._div > other._div
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self._div == 'У лектора нету оценок' or other._div == 'У лектора нету оценок':
                return 'Упс... Лектор не имеет оценки, он не поулярен :('
        return self._div < other._div
        
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            if self._div == 'У лектора нету оценок' or other._div == 'У лектора нету оценок':
                return 'Упс... Лектор не имеет оценки, он не поулярен :('
        return self._div == other._div
    
    def __ne__(self, other):
        if isinstance(other, Lecturer):
            if self._div == 'У лектора нету оценок' or other._div == 'У лектора нету оценок':
                return 'Упс... Лектор не имеет оценки, он не поулярен :('
        return self._div != other._div

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def list_studs(list_s, course):
    '''Функция высчитывает среднее у студентов, а также проверяет нахождения студента 
    в заданном списке, если нет выводит его имя и фамилию'''
    r = 0
    f = 0
    for i in list_s:
        if isinstance(i, Student):
            if course in i.courses_in_progress:
                r += sum(i.grades[course])
                f += len(i.grades[course])
            else:
                return f"Студент {i.name} {i.surname} не проходит обучение по курсу {course}"
    return r / f

def list_lect(list_s, course):
    '''Функция высчитывает среднее у лекторов, а также проверяет, обучает ли лектор, 
    в заданном списке, если нет выводит его имя и фамилию'''
    r = 0
    f = 0
    for i in list_s:
        if isinstance(i, Lecturer):
            if course in i.courses_attached:
                r += sum(i.grades[course])
                f += len(i.grades[course])
            else:
                return f"Лектор {i.name} {i.surname} не обучает {course}"
    return r / f


student_1 = Student('Rail', 'Gaifullin', 'М')
student_1.courses_in_progress += ['Python', 'Git', 'OOP']
student_1.finished_courses += ['Введение в учебу']

student_2 = Student('Anya', 'Gaifullina', 'Ж')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в учебу']

student_3 = Student('Madina', 'Ramilevna', 'Ж')
student_3.courses_in_progress += ['Введение в учебу']

lecturer_1 = Lecturer('Oleg', 'Buligin')
lecturer_1.courses_attached += ["Python", "OOP"]

lecturer_2 = Lecturer('ALena', 'Batistkaya')
lecturer_2.courses_attached += ['Git']

lecturer_3 = Lecturer('Cherni', 'Vlastelin')      # <--- Странный лектор, не умеет обучать :(
lecturer_3.courses_attached += ['Python', 'Git']

reviewer_1 = Reviewer('Zloy', 'Chelovek')
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_1, 'Git', 4)

student_1.rate_l(lecturer_1, 'Python', 10)
student_1.rate_l(lecturer_1, 'OOP', 8)
student_1.rate_l(lecturer_2, 'Git', 5)
student_1.rate_l(lecturer_3, 'Python', 2)  
student_1.rate_l(lecturer_3, 'Git', 1)
student_2.rate_l(lecturer_1, 'Python', 8)
student_2.rate_l(lecturer_3, 'Python', 4)

print(student_1._div)
print(student_2._div)
print(student_3._div)

print(lecturer_1._div)
print(lecturer_2._div)
print(lecturer_3._div)

print(student_1)
print(student_2)
print(student_3)

print(lecturer_1)
print(lecturer_2)
print(lecturer_3)

print(student_1 == student_2)
print(student_2 < student_3)
print(student_2 == student_3)
print(student_1 > student_2)

print(lecturer_1 == lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_3)
print(lecturer_1 > lecturer_3)

print(list_studs([student_1, student_2], 'Python')) # Тут студенты обучаются по курсу и у них есть оценки по Python
print(list_studs([student_1, student_2, student_3], 'Python'))  # Тут студент 3 не обучается по курсу Python

print(list_lect([lecturer_1, lecturer_3], 'Python')) # Тут оба лектора преподают Python
print(list_lect([lecturer_1, lecturer_2, lecturer_3], 'Python')) # Тут лектор 2 не преподает Python














