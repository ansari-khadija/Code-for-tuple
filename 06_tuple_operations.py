# Tuple Operations

tuple1 = ("Python", "Java", "C++")
tuple2 = ("SQL", "HTML", "CSS")

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# 1. Concatenation
print("\n--- Concatenation ---")

combined = tuple1 + tuple2
print("Combined tuple:", combined)


# 2. Repetition
print("\n--- Repetition ---")

repeated = ("Python", "Java") * 2
print("Repeated tuple:", repeated)


# 3. Membership operator
print("\n--- Membership ---")

print("Python" in tuple1)
print("SQL" in tuple1)


# 4. Not in operator
print("\n--- Not in ---")

print("HTML" not in tuple1)
print("Java" not in tuple1)


# 5. Length of tuple
print("\n--- Length ---")

print("Length of tuple1:", len(tuple1))
print("Length of tuple2:", len(tuple2))
print("Length of combined tuple:", len(combined))
