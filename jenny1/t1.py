n=int(input("enter number: "))

while 100<n<999 :
    print((n%10) + (n//100) + (n//10%10))
    n=int(input("enter number: "))

print("error")