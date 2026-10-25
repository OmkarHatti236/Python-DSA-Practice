"""
*
**
***
****
*****
"""
def right(x):
    for i in range(x+1):
        print("* "*i)

#right(5)

"""
*****
*   *
*   *
*   *
*****
"""
def rect(n, m):
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1 :
                print("*", end='')
            else:
                print(" ", end='')
        print('\n')

rect(4,5)
a=10
print(id(a))
print(id(10))
