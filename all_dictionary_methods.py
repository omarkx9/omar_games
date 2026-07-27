# ------------------------
# -- DICTIONARY METHODS --
# ------------------------

def separator():
    print("=" * 40)

separator()

# ========================================
# 1. dict.get()
# Get the value by key
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
}

print(numbers.get("one"))

# or
print(numbers["one"])

separator()

# ========================================
# 2. dict.keys()
# Return all keys
names = {
    "omar": 155,
    "islam": 23,
    "mahmoud": 34,
}

print(names.keys())

separator()

# ========================================
# 3. dict.values()
# Return all values
names = {
    "omar": 155,
    "islam": 23,
    "mahmoud": 34,
}

print(names.values())

separator()

# ========================================
# 4. dict.clear()
# Remove all items from the dictionary
names = {
    "omar": "hassan",
    "saleh": "basal",
}

names.clear()

print(names)

separator()

# ========================================
# 5. dict.update()
# Add or update key-value pairs
names = {
    "omar": "hassan"
}

names.update({"age": 14})

print(names)

# or

names["country"] = "Saudi Arabia"

print(names)

separator()

# ========================================
# 6. dict.copy()
# Create a copy of the dictionary
numbers = {
    "one": 1,
    "two": 2,
    "three": 3
}

number = numbers.copy()

print("Before:")
print(numbers)
print(number)

print("After:")

numbers.update({"four": 4})

print(numbers)
print(number)

separator()

# ========================================
# 7. dict.setdefault()
# Get a value, and if the key does not exist,
# add the key with a default value.
user = {
    "name": "omar"
}

print(user)

print(user.setdefault("name", "omar"))

print(user)

print(user.setdefault("age", 14))

print(user)

separator()

# ========================================
# 8. dict.popitem()
# Remove and return the last inserted key-value pair
dictionary = {
    "name": "omar",
    "age": 34
}

dictionary["country"] = "Saudi Arabia"

print(dictionary)

print(dictionary.popitem())

print(dictionary)

separator()

# ========================================
# 9. dict.items()
# Return all key-value pairs
dictionary = {
    "name": "omar",
    "age": 34
}

print(dictionary.items())

separator()

# ========================================
# 10. dict.fromkeys()
# Create a new dictionary from a sequence of keys
students = ["omar", "fathi", "yusuf", "hassan"]

grades = dict.fromkeys(students, 0)

print(grades)

separator()

# ========================================
# 11. dict.pop()
# Remove a specific key and return its value
user = {
    "omar": "AI",
    "hassan": "STC",
}

print(user)

print(user.pop("omar"))

print(user)

separator()