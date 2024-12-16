# Write code to assign one more user and their values, and then print out their locker number using
# a print statement.

class Student:
    def __init__(self, gradePercent, absences, locker, graduationYear):
        self.gradePercent = gradePercent
        self.absences = absences
        self.locker = locker
        self.graduationYear = graduationYear

john = Student(80, 2, 304, 2025)
eric = Student(85, 0, 293, 2025)