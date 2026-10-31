#code for given number is palindrome or npot
def palindrom(n):
    copy=n
    reverce=0
    while(n>0):
        reminder=n%10
        reverce=(reverce*10)+reminder
        n//=10
    if copy==reverce:
        return 1
    else:
        return 0


N=int(input("Enter Number:"))
if palindrom(N):
    print("Given Number is Palindrome")
else:
    print("Not Palindrome")