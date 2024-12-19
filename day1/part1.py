import numpy as np


#read file
with open("day1/input.txt", "r") as file:
    data = file.readlines()

#define list
list1 = []
list2 = []

for line in data:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

#sort list
list1.sort()
list2.sort()

#convert to npArray
array1 = np.array(list1)
array2 = np.array(list2)

#compute abs diff
list3 = np.abs(array1 - array2)
list3sum = sum(list3)

print(list3sum)