# -----------------------
# ----- SET METHODS -----
# -----------------------

# 1. set.clear()
# Remove all items
nothing = {"omar", "hassan", 4, 4.4, True}
nothing.clear()
print(nothing)

# -----------------------

# 2. set.union() ( | )
# Return a new set
no = {1, 2, 3, 4}
no2 = {1, 2, 3, 4, 5, 6, 7}
no3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(no.union(no2, no3))
print(no | no2)

# -----------------------

# 3. set.add()
# Add one item
numbers = {1, 2, 3, 4}

numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(4)
numbers.add(5)

print(numbers)

# -----------------------

# 4. set.copy()
# Copy the set
names = {"omar", "hassan", "saleh", "mahmoud"}

copy = names.copy()

names.clear()

print(copy)
print(names)

# -----------------------

# 5. set.remove()
# Remove item (Error if not found)
numbers = {1,2,3,4,5,6,7,8,9,10,11}

numbers.remove(11)

print(numbers)

# -----------------------

# 6. set.discard()
# Remove item (No Error if not found)
numbers = {1,2,3,4,5,6,7,8,9,10,11}

numbers.discard(11)
numbers.discard(34)

print(numbers)

# -----------------------

# 7. set.pop()
# Remove random item
names = {"omar", "hassan"}

names.pop()

print(names)

# -----------------------

# 8. set.update() ( |= )
# Update the original set
a = {"omar", "saleh"}
b = {"hassan"}

a.update(b)
a.update("omar")
a.update(["omar"])

print(a)

# -----------------------

# 9. set.difference() ( - )
# Return items in the first set only
items = {1, 2, "omar", "hassan", "o", "m"}
items3 = {1, 2, "omar", "hassan"}

print(items)
print(items.difference(items3))
print(items - items3)

# -----------------------

# 10. set.difference_update() ( -= )
# Remove common items from the original set
items = {1, 2, "omar", "hassan", "o", "m"}
items3 = {1, 2, "omar", "hassan"}

print(items)

items.difference_update(items3)

print(items)

# -----------------------

# 11. set.intersection() ( & )
# Return common items
items = {"omar", 4, 43, 3, 6, "hassan", "saleh"}
items2 = {"omar", 4, 43, 3, 86, "hassan", "salehب"}

print(items)

print(items.intersection(items2))
print(items & items2)

print(items)

# -----------------------

# 12. set.intersection_update() ( &= )
# Keep only common items
items = {"omar", 4, 43, 3, 6, "hassan", "saleh"}
items2 = {"omar", 4, 43, 3, 86, "hassan", "salehب"}

print(items)

items.intersection_update(items2)

print(items)

# -----------------------

# 13. set.symmetric_difference() ( ^ )
# Return non-common items
item = {"omar", "hassan", "saleh", 3, 4}
items = {"omar", "hassan", "f", 3, 4}

print(item)

print(item.symmetric_difference(items))
print(item ^ items)

print(item)

# -----------------------

# 14. set.symmetric_difference_update() ( ^= )
# Keep only non-common items
item = {"omar", "hassan", "saleh", 3, 4}
items = {"omar", "hassan", "f", 3, 4}

print(item)

item.symmetric_difference_update(items)

print(item)

# -----------------------

# 15. set.superset()
# If all valu in set1 it's in set2
a = {"omar",1,3}
b = {"omar",1,3}
c = {"omar",3,4}

print(a.issuperset(b))
print(a.issuperset(c))

# -----------------------

# 16. set.issubset()
# If all valu in set2 is in set1
a = {"omar",1,3}
b = {"omar",1,3}
c = {"omar",3,4}

print(a.issubset(b))
print(a.issubset(c))

# -----------------------

# 17. set.isdisjoin()
# If the valu disjoin 
a = {1,2,3,4}
b = {1,2}
c = {10,11,12,13}

print(a.isdisjoint(b))
print(a.isdisjoint(c))