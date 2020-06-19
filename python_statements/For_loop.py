my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    if num%2==0:
        print(num)


list_sum=0
for num in my_list:
    list_sum=list_sum+num
print(list_sum)

for letters in 'Hello World':
    print('Shibin')

#Tuple Unpacking

my_list = [(1,2),(3,4),(5,6),(7,8)]
for a,b in my_list:
    print(b)

#Iterate through Dictionary

d = {'k1':100,'k2':200,'k3':300}
for key,value in d.items():
    print(key)







