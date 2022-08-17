D=int(input("please enter the day: "))
M=int(input("please enter the month: "))
Y=int(input("please enert the year: "))
#2001
#2001%100=1 ככה לקלוט את המספר האחרון
#2001//10=200
#2001//10%10=0
#2022//10%10=2
print(f"{D}/{M}/{Y//10%10}{Y%10}")