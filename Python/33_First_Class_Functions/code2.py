def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
        else:
            raise RuntimeError(f"Could not find element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Jack Tate", "age": 30},
    {"name": "Ray Ban", "age": 27},
]


def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Rolf Smith", get_friend_name))