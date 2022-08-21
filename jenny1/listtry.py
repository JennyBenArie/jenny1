# list1=[1,2,3,4,5,6,"Hi",7,8,9,10,1,2,3]
# print(list1[6])
#
# list1.index("Hi")
# print(list1.index("Hi"))
# list1.count(100)
# print(list1.count(10))
# list1.remove(10)
# print(list1)
# print(list1.count(3))
#
# while 2 in list1 :
#     list1.remove(2)
# print(list1)

# 10 numbers rendit from1-100
from random import randint
list1=[]

for i in range(10):
    num=randint(1,100)
    list1.append(num)
print(list1)

print(list1[1:6])
print(list1[::-1])
print(list1[1:4])
print(list1[1:5:-2])