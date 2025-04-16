"""
class Pair:
    def __init__(self, person_name, yo, av_score):
        self.person_name = person_name
        self.yo = yo
        self.av_score = av_score


class Student(Pair):
    def __init__(self, person_name, yo, speciality, group, av_score):
        super().__init__(person_name, yo, av_score)
        self.speciality = speciality
        self.group = group
        self.av_score = av_score

    def __str__(self):
        return f"{self.person_name} {self.yo} {self.speciality} {self.group} {self.av_score}"


class Teacher(Pair):
    def __init__(self, person_name, yo, speciality, av_score):
        super().__init__(person_name, yo, av_score)
        self.speciality = speciality

    def __str__(self):
        return f"{self.person_name} {self.yo} {self.speciality} {self.av_score}"


class Graduate(Student):
    def __init__(self, person_name, yo, speciality, group, av_score, diploma):
        super().__init__(person_name, yo, speciality, group, av_score)
        self.diploma = diploma

    def __str__(self):
        return f"{self.person_name} {self.yo} {self.speciality} {self.group} {self.av_score} {self.av_score} {self.diploma}"


s1 = Student("Батодалаев Даши", "16", "ГК", "Web_011", 5)
print(s1)
s2 = Student("Загидуллин Линар", "32", "РПО", "PD_011", 5)
print(s2)
g1 = Graduate("Шугани Сергей", "15", "РПО", "PD_011", "5", "Защита персональных данных")
print(g1)
t1 = Teacher("Даньшин Андрей", "38", "Астрофизика", "110")
print(t1)
s3 = Student("Маркин Даниил", "17", "ГК", "Python_011", "5")
print(s3)
t2 = Teacher("Башкиров Алексей", "45", "Разработка приложений", "20")
print(t2)

"""


class Pair:
    def __init__(self, person_name, yo, av_score):
        self.person_name = person_name
        self.yo = yo
        self.av_score = av_score


class Student(Pair):
    def __init__(self, person_name, yo, speciality, group=None, av_score=None):
        super().__init__(person_name, yo, av_score)
        self.speciality = speciality
        self.group = group
        self.av_score = av_score

    def __str__(self):
        return f"{self.person_name} {self.yo} {self.speciality} {self.group} {self.av_score}"


class Teacher(Student):
    def __init__(self, person_name, yo, speciality, av_score):
        super().__init__(person_name, yo, speciality, None, av_score)

    def __str__(self):
        return f"{self.person_name} {self.yo} {self.speciality} {self.av_score}"


class Graduate(Student):
    def __init__(self, person_name, yo, speciality, group, av_score, diploma):
        super().__init__(person_name, yo, speciality, group, av_score)
        self.diploma = diploma

    def __str__(self):
        return f"{self.person_name} {self.yo} {self.speciality} {self.group} {self.av_score} {self.diploma}"


s1 = Student("Батодалаев Даши", "16", "ГК", "Web_011", 5)
print(s1)

s2 = Student("Загидуллин Линар", "32", "РПО", "PD_011", 5)
print(s2)

g1 = Graduate("Шугани Сергей", "15", "РПО", "PD_011", 5, "Защита персональных данных")
print(g1)

t1 = Teacher("Даньшин Андрей", "38", "Астрофизика", 110)
print(t1)

s3 = Student("Маркин Даниил", "17", "ГК", "Python_011", 5)
print(s3)

t2 = Teacher("Башкиров Алексей", "45", "Разработка приложений", 20)
print(t2)



