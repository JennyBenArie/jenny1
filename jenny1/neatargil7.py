N=int(input("enter number: "))

if 10<=N<=99 :
    if N//10==7 or N%10==7 or N%7==0 :
        print("lucky number")
else: print("error")
