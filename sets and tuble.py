##simple project  sets:
student1 = ("kannada","english","maths","science")
student2 = ("science","history","geography","english")
set1 = set(student1)
set2 = set(student2)
common_subjects = set1 & set2
all_subjects = set1 | set2
only_one = set1 ^ set2
only_two = set1 - set2
print("student 1 subjects:",set1)
print("student 2 subjects:",set2)
print("common subjects:",common_subjects)
print("all unique subjects:",all_subjects)
print("subjects chosen by only one student:",only_one)

##simple project tubles:
student1 = ("pallavi","4MC22CS001","BCA AI/ML")
student2 = ("bhuvan","4MC22CS002","BCA cyber security")
student3 = ("prabha","4MC22CS003","BCA data science")
print("all students:")
for s in student:
  print(s)
print("\nfirst student name:",students[0][0])
print("second student name:",students[1][1])
print("\ntotal student:",len(students))
