#--------------------
#----LIST METHODS----
#--------------------
# 1 list.append
numbers = [1,2,3,4,5,6,7]
numbers.append(8)
numbers.append(9)
numbers.append([10])
print(numbers)
# 2 list.extend()
list1 = [True,False,True,False]
list2 = [1,2,3,4,5,6,]
list3 = ["omar","hassan","saleh"]
list1.extend(list2)
list1.extend(list3)
print(list1)
# 3 list.remove()
all = [True, False, True, False, 1, 2, 3, 4, 5, 6, 'omar', 'hassan', 'saleh']
all.remove(True)
print(all)
# 4 list.sort()
numbers = [4,3,34,23,54,234,34]
numbers.sort(reverse = True)
print(numbers)
numbers.sort(reverse = False)
print(numbers)
words = ["abeer","omer","fathi","sarah","omar","yusuf","mahmoud"]
words.sort(reverse=True)
print(words)
words.sort(reverse=False)
print(words)
# 5 list.revese()
things = [True,4,"omar"]
things.reverse()
print(things)
# 6 list.clear()
money = ["in bocket","in bank","in kash"]
print("before")
print(money)
money.clear()
print("after")
print(money)
# 7 list.copy()
main_list = ["omar","omar","omar","omar"]
copied_list = main_list.copy()
print(main_list)
print(copied_list)
main_list.remove("omar")
print(main_list)
print(copied_list)
# 8 list.count()
numbers = [1,4,6,8,5,4,2,4,6,78,8,5,4,3]
print(numbers.count(4))
# 9 list.index()
numbers = [1,4,6,8,5,4,2,4,6,78,8,5,4,3]
print(numbers.index(5))
# 10 list.insert()
numbers = [1,2,4,5,6]
print(numbers)
numbers.insert(2,3)
print(numbers)
# 11 list.pop()
numbers = [1,2,3,3,4,5,6,7]
print(numbers)
numbers.pop(2)
x = numbers.pop()
print(numbers) 
print(x)