#Map:

def square(mynum):
    return mynum**2


my_num=[1,2,3,4]

for num in map(square,my_num):
    print(num)

print(list(map(square,my_num)))


