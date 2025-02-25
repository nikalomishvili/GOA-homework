
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]


numbers.append(100)
print("After append(100):", numbers)


numbers.insert(0, 5)
print("After insert(5) at the beginning:", numbers)


numbers.remove(30)
print("After remove(30):", numbers)


numbers.sort()
print("After sort():", numbers)


numbers.reverse()
print("After reverse():", numbers)


index_50 = numbers.index(50)
print("Index of 50:", index_50)


count_20 = numbers.count(20)
print("Count of 20:", count_20)