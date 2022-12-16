print("")
print("****************************")
print("* Printing")
print("****************************")
print("")

price = 9.99
print ("Price")
print (price)
print("Price", price) 

discount = .25
print ("Discount")
print(discount)

discount_price = price * (1-discount)

print ("discount price", discount_price)


print("")
print("****************************")
print("* Print Variables")
print("****************************")
print("")
name = 'jack'
print (name)
name = 'bob'
print (name)

print("")
print("****************************")
print("* Print with f string functions")
print("****************************")
print("")

greeting = f'hello, {name}'
print (greeting)
name = 'jack'
print(f'hello, {name}')

print("")
print("****************************")
print("* Print with templating functions")
print("****************************")
print("")

print("using templating and phrasing")

name = 'ed'
greeting = 'Hello, {}'  # template for greeting
with_name = greeting.format(name)
with_name_2 = greeting.format('bill')
print(with_name)
print(with_name_2)

longer_phrase = 'Hello, {}.  Today is {}'
formated_phrase = longer_phrase.format('Art', 'Monday')
print(formated_phrase)

print("")
print("****************************")
print("")