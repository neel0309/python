dict = {"Alice": 1, "Bob": 2, "Charlie": 3,"Neil": 3}


take = input(f"Enter the student's name:")

for name in dict:
    if name == take:
        print(f"{name} marks: {dict[name]}")

