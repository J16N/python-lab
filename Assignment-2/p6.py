def status(age):
    status = ""
    if (age == 1):
        status = "in born"
    elif (age >= 2 and age <= 10):
        status = "child"
    elif (age >= 11 and age <= 17):
        status = "young"
    elif (age >= 18 and age <= 49):
        status = "adult"
    elif (age >= 50 and age <= 79):
        status = "old"
    else:
        status = "very old"
    return status

age = int(input("Enter the age: "))
print("Status:", status(age))