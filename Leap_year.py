def leap(year):
    if year%4==0:
        if year%100==0:
            return year%400==0
        return True
    return False

y=int(input("Enter year:"))
if leap(y):
    print("yes Leap year")
else:
    print("not leap year")