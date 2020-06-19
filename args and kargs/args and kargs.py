#args
def addition(*args):
    return sum(args) + 0.05

print(addition(20,30,50))

#kwarks
def multipledata(**kwargs):
    print(kwargs)

multipledata(name='Shibin',Age=20,Place='Chennai')