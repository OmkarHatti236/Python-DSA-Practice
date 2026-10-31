def isPalindrome(s):
    
    new=''
    for i in s:
        if i.isalnum():
            new+=i.lower()
    start=0
    end=len(new)-1
    while start<end:
        if new[start]==new[end]:
            start+=1
            end-=1
            continue
        else:
            return False
    return True

s="A man, a plan, a canal: Panamaa" 
if isPalindrome(s):
    print("Palindrome")
else:
    print("not Palindrome")