StudentName = ["bobinder", "lindajit", "davepal"]
StudentMark = [[25,35,45], [12,34,56]]
ClassSize = 3
SubjectNo = 2

#total mark for each student for all subjects
average_mark = []
def totalMark():
    for student in ClassSize:
        print(student)
        index_stud = StudentName.index(student)

        for subject in StudentMark:
            average_mark.append(subject[index_stud] in range(len(StudentMark)))
            print(subject[index_stud] in range(len(StudentMark)))
            print(average_mark)

totalMark()


