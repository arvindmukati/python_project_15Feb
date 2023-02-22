colors = ["Red", "Blue", "White"]
print(colors[1])
print(type(colors))
colors.append("Pink")
print(colors)
# insert black in list
colors.insert(1, "Yellow")
print(colors)
# remove white from list
colors.remove("White")
print(colors)
removed = colors.pop()
print("Removed Items", removed)
print(colors)

numbers = [22.5, 12, 34, 11.2]
print(type(numbers))
print(type(numbers[0]))
students = {99: "Ad","name": "Arvind", "emailId": "abc@gmail.com", "marks": [98, 70, 100, 10], "sports":{"indoor":"hockey","outdoor":"hockey"}}
print(students)
print(type(students))
print(students["marks"])
print(type(students["marks"]))
print(students["marks"][0])
marks = students["marks"]
print(marks[1])
print(students["sports"]["indoor"])
print(students[99])