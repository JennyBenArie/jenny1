grade= int(input("please enter garde: "))
name= str(input("pleasr enter name:"))

if 0<grade<100 :
    if grade>=70 and (name== "Dan" or name== "Dana") :
        print("student passed the test")
    else : print("failed")
else: print("arror")