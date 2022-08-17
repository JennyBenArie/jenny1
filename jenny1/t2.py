age = int(input("enter age: "))
count=0

while 0>age and age<120 :
    count+=1
    if count==3:
      print("error")
else:
    age = int(input("enter age: "))

if 0 <= age <= 18:
    print(f" {age} is an age of a child.")
elif 19 <= age <= 60:
    print(f" {age} is an age of a adult. ")
elif 61 <= age <= 120:
    print(f" {age} is an age of a senior. ")
    age = int(input(" enter age: "))