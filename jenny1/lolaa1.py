# targil 1
## summ=0

# for i in range (6):
#     num=int(input(f"enter number {i+1} :"))
#     summ+=num
#
# print("total: ", summ)
# print("avarge:", summ/6)
# ======================================
# targil 2
# total=0
# count=0
# for i in range (6):
#      num=int(input(f"enter number {i+1} :"))
#      if num%2==0 :
#          total+=num
#          count+=1
# print("total:", total)
# print("avarge: ", total/count)
# ========================================
#targil 3
# for i in range(10,100):
#     if i%10==7 :
#         print(i)
#============================================
#targil 4
# total = 0
# for i in range (10 , 100):
#     if i%10==0:
#         total+=i
# print("total: ", total)
# =========================================
# targil 5
# grade=int(input("enter grade: "))
# total=0
# count=0
# while 0<=grade<=100 :
#     if grade>=60:
#         total+=grade
#         count+=1
#     grade = int(input("enter grade: "))
#
# print("avarge: ", total/count)
# ===============================================
#
# targil 6# grade=int(input("enter grade: "))
# total=0
# count=0
# total1=0
# count1=0
# while 0<=grade<=100 :
#     if grade>=60:
#         total+=grade
#         count+=1
#     grade = int(input("enter grade: "))
#     if grade<60:
#         total1+=grade
#         count1+=1
#     grade = int(input("enter grade: "))
#
# print("passed avarge: ", total/count)
# print("failed avarge: ", total1/count1)
# =========================================
# targil 7
# total=0
# total1=0
# for i in range (5):
#     num=int(input(f"enter number {1+i}: "))
#     if num>=10:
#         num=num%10
#         total+=num
#     else:
#        num=num
#        total1+=num
#
# print("total number of right digits is: ", total+total1)
# =========================================================
# targil 8
# num=int(input("enter number: "))
#
# for i in range (1,num):
#     if i%5==0 :
#         print(i)
# =================================================================
# targil 9
# num=int(input("enter number: "))
# #
# # for i in range (2,num,2):
# #     print(i)
# # ===============================================================
# targil 10
# num=int(input("enter number: "))
# total_numbers=0
# while num!=0 :
#     if num%3==0 or num%7==0 :
#         total_numbers+=1
#     else:
#         total_numbers=0
#     num = int(input("enter number: "))
# print(f"there are {total_numbers} that split with 7 or 3")
# ================================================================
# targil 3.1
# num=int(input("enter number: "))
# num2=int(input("enter number 2: "))
#
# for i in range ((num+1),num2,):
#     if i%2==0:
#         print(i)
# ===========================================================
# targil3.2
# num=int(input("enter positive number: "))
#
# for i in range(2,num):
#     if num%i==0 :
#         print("this is not the number")
#         num = int(input("enter number: "))
# print("this is the number!!")
# ===============================================================
# targil3.3
# from random import randint
# ran_num=randint(1,9)
#
# guess=int(input("guess number between 1-9: "))
#
# while ran_num!= guess :
#     if ran_num<guess:
#         print("the number you guessed is bigger than the number")
#         guess = int(input("guess number between 1-9: "))
#     elif ran_num>guess:
#         print("the number you guessed is lower than the number")
#         guess = int(input("guess number between 1-9: "))
# else: print("this is the currect number!")
# ====================================================================
# targil3.4

# Try=0
# guess=int(input("choose number between 1-100: "))
# while 0<=guess<=100:
#     ran = randint(1, 100)
#     print("system's guess: ", ran)
#     system_guess=int(input("if the number is bigger than you number, press 1.\nif the number is lower than your number press 2.\nif the number is your number, press 3."))
#     if system_guess==1:
#         Try+=1
#     elif system_guess==2:
#         Try += 1
#     if system_guess==3:
#         print(f"system currect!, after {Try} times")
#         break
# =================================================================================
# targil 3.5
num=int(input("enter how many digits will be in the series: " ))
fn=0
sn=1
for i in range(num):
    if i==0:
        print(fn)
        continue
    print(sn)
    nn=sn+fn
    fn=sn
    sn=nn