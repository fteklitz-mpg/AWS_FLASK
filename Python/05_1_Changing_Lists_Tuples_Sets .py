print("")
print("****************************")
print("* Collections: Lists, Tuples, and Sets")
print("* A collection is a variable with multiple items for different use cases")
print("****************************")
print("")
print("Print code: list_l = ['bob', 'tom', 'bill']")
print("")

list_l = ['bob', 'tom', 'bill']
print (list_l)

print("")
print("Print code: tuple_t = ('jane', 'jan', 'joy')")
print("")

tuple_t = ('jane', 'jan', 'joy')
print (tuple_t)

print("")
print("****************************")
print("* Change a list element - item assignment")
print("* A collection is a variable with multiple items for different use cases")
print("****************************")
print("")
print("* Print code: list_l[0] = 'Robby' ")
print("")

list_l[0] = 'Robby'
print(list_l)

#cannot change a tuples element (but can assign a value)
# tuple_t[0] = 'ann'
# print(tuple_t)

print("")
print("****************************")
print("* cannot change a tuples element (but can assign a value) ")
print("* A collection is a variable with multiple items for different use cases")
print("****************************")
print("")
print("* Print code: tuple_t[0] = 'ann' ")
print("")


tuple_t[0] = 'ann'
print(tuple_t)

print("")
print("* remove elements ")
print("* list_l.remove(/"bob/") ")
print("")

list_l = ['bob', 'tom', 'bill']
list_l.remove("bob")
print(list_l)

print("* can add to sets (vs append) ")
print("* Code: set_s.add(/"george/") ")
print("")
set_s = {'bob', 'tom', 'bill'}
set_s.add("george")
print(set_s)

# in keyword checks for membership in a collection

list_l = ['bob', 'tom', 'bill']
print("bob" in list_l)

movies_watched = {"The Batman", "Don't Look Up", "Year of the Dog"}
user_movie = input("enter a movie: ")

print(user_movie in movies_watched)

