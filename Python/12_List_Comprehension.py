# List Comprehension 

numbers = [1,3,5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)

# Comprehension Example 1
numbers = [1,3,5]
doubled = [num * 2 for num in numbers]

print(doubled)


# Comprehension Example 2

## using for loop

friends = {'bob', 'bill', 'sid', 'jack'}
starts_s = []

for friend in friends:
    if friend.startswith('b'):
        starts_s.append(friend)

print(starts_s)

## using list comprehension

friends = ['bob', 'bill', 'sid', 'jack']
starts_s = [friend for friend in friends if friend.startswith('b')]

print(f"friends is {friends}")
print(f"starts_s is {starts_s}")
print(friends is starts_s)
print('friends: ', id(friends), 'starts_s: ', id(starts_s) )

