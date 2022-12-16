# Dictionaries for key: value pairs
# keys can be strings, integers or hashable types

friend_ages = {"jack": 24, "adam": 30, "anne": 37}

# add a key 

friend_ages = {"bill": 20}

# change a key 

friend_ages = {"jack": 21}

# list of dictionaries

friends = [
    {"name": "bill", "age": "24"},
    {"name": "Adam", "age": "30"},
    {"name": "Anne", "age": "27"},
    {"name": "Greg", "age": "25"}
]

print(friends)
print(friends[0])
print(friends[0]["name"])
print(friends[0]["age"])
print("my frield is {0}. He is {1} years old".format(friends[0]["name"], friends[0]["age"]))

# Dictionary of 3 dictionaries

myfamily = {
  "child1" : {
     "name" : "Emil",
     "year" : 2004
  },
  "child2" : {
     "name" : "Tobias",
     "year" : 2007
  },
  "child3" : {
     "name" : "Linus",
     "year" : 2011
  }
}

# 3 Dictionaries combined 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# Dictionary version 1

student_attendance = {"jack": 96, "adam": 80, "anne": 100}

for student in student_attendance:
    print(student)
    
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# Dictionary version 2

student_attendance = {"jack": 96, "adam": 80, "anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# Use in to check for keys

student_attendance = {"jack": 96, "adam": 80, "anne": 100}

if "jack" in student_attendance:
    print(f"jack: {student_attendance['jack']}")
else:
    print("jack is not a student in this class.")


# Use in to check for keys

student_attendance = {"jack": 96, "adam": 80, "anne": 100}

student = "bill"

if student in student_attendance:
    print(f"{student}: {student_attendance['jack']}")
else:
    print(f"{student} is not a student in this class.")


student_attendance = {"jack": 96, "adam": 80, "anne": 100}
attendance_value = student_attendance.values()
print (sum(attendance_value) / len(attendance_value))