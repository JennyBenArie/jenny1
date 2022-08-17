D=int(input("enter Day: "))
M=int(input("enter Month: "))
Y=int(input("enter Year: "))

if 1<=D<=31 :
    if D<10:
        D=f"0{D}"
    if 1<=M<=12 :
        if M<10:
            M=f"0{M}"
        if 1950<=Y<=2020:
            print(f"{D}/{M}/{Y%100//10}{Y%10}")
        else: print("error, please enter new year")
    else: print("error, please enter new month")

else: print("error, please enter new day")


#another option
day= int(input("enter day: "))
month= int(input("enter month: "))
year= int(input("enter year: "))

while day<1 or day>31:
    print("please enter day currectly")
    day= int(input("enter day: "))

while month < 1 or month > 12:
    print("please enter month currectly")
    month = int(input("enter month: "))

while year < 1950 or year > 2020:
    print("please enter year currectly")
    year = int(input("enter year: "))
if day<10:
        day=f"0{day}"
        if month<10:
            month=f"0{month}"
            print(f"{day}/{month}/{year%100//10}{year%10}")


