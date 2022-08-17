three_number=int(input("please enter three digits number:"))
#487
n1=three_number%10
n2=three_number//10%10
n3=three_number//100
print(f"{n1}{n2}{n3}")