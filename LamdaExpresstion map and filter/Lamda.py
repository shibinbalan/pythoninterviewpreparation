#Map:
def square(my_num):
    return my_num**2

num = [1,2,3,4,5,6]
for numbers in map(square,num):
    print(numbers)

print(list(map(square,num)))

#Another Method

def eve_string(my_string):
    if len(my_string)%2==0:
        return 'EVEN'
    else:
        return my_string[0]

strin=['Shibin','Diljith','Shyamala']

print(list(map(eve_string,strin)))


#Filter Function
def is_even(num):
    return num%2==0

numbers = [20,30,40,58,51]
print(list(filter(is_even,numbers)))
#Lamda
def is_even(numbers):
    return numbers**2
#converting the above function into lambda

square = lambda numbers: numbers**2

print(list(map(lambda numbers: numbers**2,numbers)))






















