#EXERSICE 1
students = ["Marcos", "Mayra", "Tom", "Samantha"]

print(students[1])
print(students[-1])


# EXERSICE 2

foods = ('tacos', 'pizza', 'burger', 'burrito')

print(foods)

for f in foods:
    print(f'{f} is a good food')

# EXERSICE 3

for f in foods:
    print(foods[2:])

# EXERSICE 4    

home_town = {
    'city': 'Chicago',
    'state': 'Illinois',
    'population': 271,
}

print(f"I was born in {home_town['city']},{home_town['state']}-population of {home_town['population']}.")

# Exersice 5


for key, val in home_town.items():
    print(f"{key} = {val}")  

# EXERSICE 6      


cohort = []

for index, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index]
    })

for student in cohort:
    print(student)

#EXERSICE 7    

awesome_students = [f'{name} is awesome!'for name in students]

for students in  awesome_students:
    print(student)

# EXERSICE 8

a_foods = [food for food in foods if "a" in food]
print(a_foods)

