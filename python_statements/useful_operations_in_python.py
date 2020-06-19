#Range

for num in range(0,10,2):
    print(num)

#Enumerate-> which is used to find the index position of an element
my_string = 'Shibin'
for a,b in enumerate(my_string):
    print(a)

#Zip Function

my_list1 = ['a','b','c','d']
my_list2 = [1,2,3,4]
for ele in zip(my_list1,my_list2):
    print(ele)


#in Keyword
#Built in min function

#Random Library
from random import shuffle
my_li = [2,5,6,4,7,8,9]
shuffle(my_li)
print(my_li)