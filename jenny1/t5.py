n1 = int(input("enter number 1: "))

while 10<n1<99 :
    if n1//10 == 7 or n1%10 == 7 or n1%7 == 0 :
        print("this is a lucky number")

    else: print("try to enter a lucky number")
    n1 = int(input("enter number 1: "))