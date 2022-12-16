# loop through list of friends

friends = ['bob', 'bill', 'sid', 'jack']

for friend in friends:
    print(f"{friend} is my friend")

# loop through list of grades

grades = [35, 67, 96, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(f"grade average is {total / amount}")

# sum function

grades = [35, 67, 96, 100, 100]
amount = len(grades)
total = sum(grades)

print(f"grade average is {total / amount}")