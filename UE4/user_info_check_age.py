def get_person_info():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    return {"first_name": first_name, "last_name": last_name, "age": age}

people = [
    {"first_name": "Ramin", "last_name": "Kasumov", "age": 19},
    {"first_name": "Dario", "last_name": "Stromajer", "age": 20},
    {"first_name": "Thimon", "last_name": "Pelka", "age": 23},
]

all_adults = all(person["age"] >= 18 for person in people)
print("All are adults:", all_adults)