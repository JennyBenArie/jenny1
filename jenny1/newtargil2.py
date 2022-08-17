N=int(input("enter number: "))

if 100<=N<=999:
    print((N//100)+(N//10%10)+(N%10))

else: print("error")

