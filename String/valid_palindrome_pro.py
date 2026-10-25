def palindrom_check(string):
    new = ''.join(ch.lower() for ch in string if string.isalnum())
    return new==new[::-1]

s="8A man, a plan, a canal: Panamaz8"
if palindrom_check(s):
    print("yes palindrom")
else:
    print("not palindrome")
