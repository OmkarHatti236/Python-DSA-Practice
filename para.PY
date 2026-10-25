
def validPara(para):
    pairs = {"(": ")", "[": "]", "{": "}"}
    if len(para)%2!=0:
        return False
    add=[]
    for i in para:
        if(pairs.get(i)):
            add.append(pairs.get(i))
            print(add)
        else:
            if len(add)>0:
                last=add.pop()
                if(i==last):
                    continue
                else:
                    return False
            else:
                return False
    return len(add)==0
print(validPara("))"))


class Solution(object):
    def isValid(self, s):
        # Early exit for odd length
        if len(s) % 2 != 0:
            return False

        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            # If opening bracket → push
            if ch in pairs.values():
                stack.append(ch)
            else:
                # Closing bracket must match top of stack
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack