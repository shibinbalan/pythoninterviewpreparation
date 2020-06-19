#list of numbers
my_num = [1,2,3,4,5]
listsum=0
for num in my_num:
    listsum=listsum+num

    print(listsum)


for num in range(0,6):
    listsum=listsum+num

    print(listsum)

#Tuple Unpacking

my_list = [(1,2),(3,4)]
for a,b in my_list:
    print(a)
    print(b)

my_dict = {'k1':100,'k2':200,'k3':300}
for key,items in my_dict.items():
    print(my_dict)

