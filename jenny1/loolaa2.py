# grade=int(input("enter grade: "))
# highest=0
# total = 0
# count=0
# while 0<=grade<=100:
#     if grade>highest:
#         highest=grade
#     count+=1
#     total+=grade
#     grade = int(input("enter grade: "))
# print("highest grade: ",highest)
# print("avarge grade: ",total/count)
# print("the diffrence between the highest grade to the avarge is: ", highest-(total/count))
# ========================================================================
# targil2
# password=int(input("enter password: "))
# password2=int(input("enter same password: "))
#
# for i in range(5):
#     if password!=password2:
#         print("try again.")
#
#     else:
#         print("password saved !")
#         break
#     password2 = int(input("enter same password: "))
# else:
#     print("inccurect paswword.")
# ==================================================================
# targil3
num=int(input("enter number: "))
count=0
while num//10!=0:
    count+=num%10
    num=num//10
count+=num
print("the digits sum is:", count)

