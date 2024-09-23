import random

def pick_stick():
    # Here we open the files
    openStudentListRaw = open("student_list", "r")
    openAlreadyCalled = open("already_called", "r")

    # This makes it so that the files are read as strings
    studentListRaw = openStudentListRaw.read()
    alreadyCalledRaw = openAlreadyCalled.read()

    # This converts them to Python lists
    studentList = studentListRaw.splitlines()
    alreadyCalled = alreadyCalledRaw.splitlines()

    # This randomly picks a student from the list
    popsicle_stick = random.choice(studentList)

    # This checks if the student name is not in the already called list, and if not, it adds it to the already called list and prints out the name
    if popsicle_stick not in alreadyCalled:
        with open("already_called", "a") as ac:
            ac.write(popsicle_stick + "\n")
            print(popsicle_stick)
    # This checks if the student list and already called list are the same when sorted, and if they are, it prints out that all the students have been called
    elif sorted(alreadyCalled) == sorted(studentList):
        print("All students have been called. Clearing file...")
        with open("already_called", "w") as ap:
            ap.truncate(0)
        print("File cleared. Choosing from list")
        pick_stick()
    # If the student name is in the already called list, close the file and call the function again
    elif popsicle_stick in alreadyCalled:
        openStudentListRaw.close() # While not strictly necessary, as we're not writing to this file, it's still good practise to close the file
        pick_stick()

pick_stick()