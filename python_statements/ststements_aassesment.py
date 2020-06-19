#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
st=st.split()
for char in st:
    if char[0]=='s':
        print(char)

#Use range() to print all the even numbers from 0 to 10.
for num in range(0,101):
    if num%2==0:
        print(num)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

my_list=[num%3==0 for num in range(1,51)]
print(my_list)
#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
st=st.split()
for letters in st:
    if len(letters)%2==0:
        print(letters)


#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
my_lis = []
for letters in my_lis:
    my_lis.append(list(st[0]))

print(my_lis)