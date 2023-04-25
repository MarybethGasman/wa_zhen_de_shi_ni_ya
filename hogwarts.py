students=["Hermione", "Harry", "Ron"]

print(students)

print(students[0])

for s in students:
    print(s,id(s))
print(s)

for i in range(len(students)):
    print(i, students[i],sep="") 

print(list(range(len(students))))
# students={"Hermione":"Gryffiondor"},Harry":"Gryffindor"
students = {
    "hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
}

print(students["hermione"])

for s in students:
    print(s, students[s])

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack"},
    {"name": "Draco", "house": "Gryffindor", "patronus": None},
]

for s  in students:
    print(s["name"], s["house"], s["patronus"], sep=",")