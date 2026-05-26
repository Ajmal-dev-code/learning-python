student = {
    "name": "Devil",
    "age": 30,
    "work": "manuplating people"
}
for key in student.keys():
    print(key)

for key in student:
    print(key)

for value in student.values():
    print(value)
for key, value in student.items():
    print(key, value)