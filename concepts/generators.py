def gen():
    for i in range(100):
        yield i

print(next(gen()))
print(next(gen()))
print(next(gen()))
print(next(gen()))