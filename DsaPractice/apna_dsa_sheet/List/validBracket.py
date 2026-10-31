def isBalanced(s):
    if len(s)%2!=0:
        return "NO"
    stack=[]
    for i in s:
        if i=="(":
            stack.append(")")
        elif i=="{":
            stack.append("}")
        elif i=="[":
            stack.append("]")
        else:
            if not stack or stack.pop() != i:
                return "NO"
    return "YES" if not stack else "NO"

b="{({()})}"
value=isBalanced(b)
print(value)