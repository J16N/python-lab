ageRange = {(25, 35): 0, (36, 45): 0, (46, 55): 0}
ages = map(int, input("Enter ages (seperated by spaces): ").split())

for age in ages:
    if (25 <= age <= 35): ageRange[(25, 35)] += 1
    elif (36 <= age <= 45): ageRange[(36, 45)] += 1
    elif (46 <= age <= 55): ageRange[(46, 55)] += 1

for k, v in ageRange.items():
    lower, upper = k
    print("Employees in age group {} - {}: {}".format(lower, upper, v))
