


sum=0
for num in range(0,100):
    print(num)
    sum=sum+num
print(sum)
#while loop

x=0
while x<5:
    print('x is less than 5!!!')
    x = x+1

#break

for num in range(0,10):
    if num==2:
        break
    print(num)

#continue
my_string='Shibin'
for letters in my_string:
    if letters=='i':
        continue
    print(letters)
#Range:
#Enumarate: FInd the index position
my_stri = 'Shibin'
for a,b in enumerate(my_stri):
    print(a)
    print(b)
#Zip
my_list1 = [20,30,40]
my_list2 = [50,60,70]
for num in zip(my_list2,my_list2):
    print(num)

#List comprehenstions:
my_string = 'adipoli'
my_li = [letter for letter in my_string]
print(my_li)