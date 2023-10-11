subjectsList = ["History", "Math", "Science", "English", "Art", "PE"]
historyGrades = ["5 A's", "3 B's", "2 C's", "5 D's", "7 F's"]
mathGrades = ["25 A's", "15 B's", "13 C's", "12 D's"]
scienceGrades = ["15 A's", "23 B's", "2 C's", "5 D's", "2 F's"]
englishGrades = ["23 C's", "15 D's", "17 F's"]
artGrades = ["5 A's", "3 B's", "10 C's", "2 D's", "4 F's"]
peGrades = ["20 A's", "5 B's"]
gradeList = [historyGrades, mathGrades, scienceGrades, englishGrades, artGrades, peGrades]

for index in range(len(subjectsList)):
    print(subjectsList[index] + ":")
    for grade in gradeList[index]:
        print(grade)
    print("\n")