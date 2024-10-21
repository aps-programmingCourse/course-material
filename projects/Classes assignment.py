## Create Class

class Student:
    def __init__(self, gradePercent, absences, locker, graduationYear):
        self.gradePercent = gradePercent
        self.absences = absences
        self.locker = locker
        self.graduationYear = graduationYear

john = Student(80, 2, 304, 2025)
