n1 = int(input("enter number 1: "))
n2 = int(input("enter number 2: "))

while n1%2 == 0 and n2%2 == 0 :
    print(f"number 1 + number 2= {n1+n2}")
    n1 = int(input("enter number 1: "))
    n2 = int(input("enter number 2: "))
print(f"number 1 * number 2= {n1*n2}")