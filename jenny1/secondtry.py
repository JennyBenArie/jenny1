grade=int(input("enter grade: "))
count=0

while 0>grade or grade>120 :
    count+=1
    if count ==5 :
        print("too many trailes!!")
        break
    grade = int(input("enter grade: "))
print("error, insert valid grade")

print("====================================")
for i in range(3,100,3) :
    print(i)
print("====================================")
for i in range(2,201,2):
    print(i)
