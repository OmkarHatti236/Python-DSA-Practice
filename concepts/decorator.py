'''A decorator in Python is a function that adds extra functionality 
to another function without changing its original code.'''

def main(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper




# @main
def greet():
    print("hello omkar")


# greet = main(greet)

greet()