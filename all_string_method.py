# 1 string.capitalize()
word = "oMar hASan iS tHE BeST"
print(word.capitalize())

# 2 string.center()
name = "Omar"
print(name.center(len(name)+2,"$"))

# 3 string.count()
best_teacher = "omar,hassan,omar,saleh,fahad,omar,mourad"
print(best_teacher.count("omar"))
print(best_teacher.count("omar",0,16))

# 4 string.endswith()
word = "I'm study python"
print(word.endswith("N"))
print(word.endswith("y",0,9))

# 5 string.expandtabs()
word = "omar\thassan\tlove\tpython"
print(word.expandtabs(10))
print(word.expandtabs(10*2))
print(word.expandtabs(10*3))

# 6 string.find(substring, start, end)
names = "omar hassan mahmoud saleh"
print(names.find("saleh",0,19))
print(names.find("saleh"))

# 7 string.index(substring, start, end)
names = "omar hassan mahmoud saleh"
print(names.index("saleh"))
print(names.index("saleh",10,26))

names = ["omar","hassan","mahmoude","saleh"]
print(names.index("hassan"))
print(names.index("hassan",1,-1))

# 8 string.isalnum()
password = "Omar1234omar"
print(password.isalnum())

# 9 string.isalpha()
letters = "abcdefghigklmnopqrstuvwxyz"
print(letters.isalpha())
letters = "abcdefghigklmnopqrstuv4wxyz"
print(letters.isalpha())

# 10 string.isdigit()
number = "1234"
print(number.isdigit())

# 11 string.isidentifier()
a = "omar--omar"
c = "if"
b = "_"
print(a.isidentifier())
print(c.isidentifier())
print(b.isidentifier())

# 12 string.islower()
word = "omar"
print(word.islower())

# 13 string.isspace()
char = " "
print(char.isspace())
char = " ="
print(char.isspace())

# 14 string.istitle()
name = "My Name Is Omar 4G"
print(name.istitle())
name = "My Name Is Omar 4g"
print(name.istitle())

# 15 string.isupper()
word = "OMAR"
print(word.isupper())

# 16 string.join()
names = ["omar","hassan","mahmoud","saleh"]
print(" ".join(names))
# 17 string.lower()
word = "oMar hASan iS tHE BeST"
print(word.lower())

# 18 string.ljust(width, fillchar)
name = "Omar"
print(name.ljust(12))
print(name.ljust(12,"^"))

# 19 string.lstrip()
word = "%@           omar hassan              @%"
print(word.lstrip("%@ "))

# 20 string.replace(old, new)
numbers = "one two three one four five"
numbers = numbers.replace("one","1",1)
numbers = numbers.replace("two","2")
numbers = numbers.replace("three","3")
numbers = numbers.replace("four","4")
numbers = numbers.replace("five","5")
print(numbers)

# 21 string.rjust(width, fillchar)
name = "Omar"
print(name.rjust(12))
print(name.rjust(12,"^"))

# 22 string.rsplit()
numbers = "1 2 3 4 5 6 7"
print(numbers.rsplit())
print(numbers.rsplit(" ",2))

# 23 string.rstrip()
word = "%@           omar hassan              @%"
print(word.rstrip("%@ "))

# 24 string.split()
numbers = "1 2 3 4 5 6 7"
print(numbers.split())
print(numbers.split(" ",2))

# 25 string.splitlines()
lines = """first line
second line
third line
fourth line
"""
print(lines.splitlines())

lines = "first line\nseconde line\nthird line\nfourth line"
print(lines.splitlines())

# 26 string.startswith()
word = "I'm study python"
print(word.startswith("i"))
print(word.startswith("study",4,9))

# 27 string.strip()
word = "%@           omar hassan              @%"
print(word.strip("%@ "))

# 28 string.swapcase()
word1 = "i lOVE pYTHON"
word2 = "I Love Python"
print(word1.swapcase())
print(word2.swapcase())
# 29 string.title()
word = "oMar hASsan iS tHE BeST"
print(word.title())

# 30 string.upper()
word = "oMar hASsan iS tHE BeST"
print(word.upper())

# 31 string.zfill()
n1, n2, n3, n4, n5 = "1", "11", "111", "1111", "11111"

print(n1.zfill(5))
print(n2.zfill(5))
print(n3.zfill(5))
print(n4.zfill(5))
print(n5.zfill(5))