mondayClass = {"Alic","Bob","Claire","Dora"}
wednesdayClass = {"Alic","Bob","Eric","Frank"}

mondayClass.add("Eric")
print("Monday Class", mondayClass)
print("Wed Class", wednesdayClass)

bothClasses = mondayClass & wednesdayClass
print("Attended both class: ", bothClasses)

allStudents = mondayClass | wednesdayClass
print("all Student: ", allStudents)

onlyStudent = mondayClass ^ wednesdayClass
print("Only student: ", onlyStudent)
print("Is Monday subset of all students", mondayClass <= allStudents)