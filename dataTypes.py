# making a list called x

x = [1 ,2 ,3]

print(len(x))

# making a tuple = an immutable list

y = ("a", "b")
print(y)

# can assign multiple values to a tuple at once 
yellow = (255, 255, 0)
r, g, b = yellow
print(r, g, b)

print(yellow)

# making a dictionary, like json in JS

person = {"name": "Alice", "email": "alice@example.com"}

print(person['name'])
print(person)

# making a set, an unordered list
x = {1, 2, 3, 2, 1}
print(x)
#prints set([1,2,3])
