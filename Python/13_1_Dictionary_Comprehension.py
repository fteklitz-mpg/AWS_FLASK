# Dictionary Comprehension

users = [
    (0, "Bob", "password"),
    (1, "Jack", "Jack12"),
    (2, "Bill", "advududw"),
    (3, "username", "1234"),
]

username_mapping = {user[1]:user for user in users}

print(username_mapping)

#

users = [
    (0, "Bob", "password"),
    (1, "Jack", "Jack12"),
    (2, "Bill", "advududw"),
    (3, "username", "1234"),
]

username_mapping = {user[1]:user for user in users}

print(username_mapping["Bob"])

# password example

users = [
    (0, "Bob", "password"),
    (1, "Jack", "Jack12"),
    (2, "Bill", "advududw"),
    (3, "username", "1234"),
]

username_mapping = {user[1]:user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("your credentials are correct")
else:
    print("your credentials are incorrect")

