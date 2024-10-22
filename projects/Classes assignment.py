## Write code that will print out the locker number for john

class Student:
    def __init__(self, gradePercent, absences, locker, graduationYear):
        self.gradePercent = gradePercent
        self.absences = absences
        self.locker = locker
        self.graduationYear = graduationYear

john = Student(80, 2, 304, 2025)
eric = Student(85, 0, 293, 2025)