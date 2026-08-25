# Tuple Packing and Unpacking

# Tuple Packing
print("--- Tuple Packing ---")

student = ("Rahul", 20, "Pune", "Python")

print("Student tuple:", student)


# Tuple Unpacking
print("\n--- Tuple Unpacking ---")

name, age, city, course = student

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)


# Unpacking numbers
print("\n--- Unpacking Numbers ---")

numbers = (10, 20, 30, 40, 50)

a, b, c, d, e = numbers

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)


# Extended unpacking
print("\n--- Extended Unpacking ---")

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)
