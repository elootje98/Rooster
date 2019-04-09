import data as d

for i in d.Classrooms:
    print(d.Classrooms[i])

for j in d.Courses:
    print(d.Courses[j])

d.Classrooms["A1.06"].assign_slot("Tu11", "Algoritmen en complexiteit",
    d.Courses["Algoritmen en complexiteit"].lectures[0])

print(d.Classrooms["A1.06"])
