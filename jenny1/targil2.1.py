N=int(input("please enter number: "))
if N%2==0:
    print("number is even")
else:print("number isn't even")

#2.2
N1=int(input("enter number 1: "))
N2=int(input("enter number 2: "))
N3=int(input("enter number 3: "))

if N1>N2 and N1>N3:
    print(N1)
if N2>N1 and N2>N3 :
    print(N2)
if N3>N1 and N3>N2:
    print(N3)


#2.3
N=int(input("please enter number: "))
if N=="":
    N==15
print(f"tomrrow you need to do {N*2}")
