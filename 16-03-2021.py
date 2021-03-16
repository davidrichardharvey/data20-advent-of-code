# Enumerate

data20 = ['Reece', 'Matt', 'Adam', 'Mark', 'Rachel', 'Victor']

for person in data20:
    print(person)

for i in range(len(data20)):
    print(i, data20[i])

# Why not both at the same time?
for i, person in enumerate(data20):
    print(f"{person} is at index position {i}")

# List Comprehension

data20initial = []
for person in data20:
    data20initial.append(person[0])
data20initial = ''.join([person[0] for person in data20])
print(data20initial)
print(data20)
