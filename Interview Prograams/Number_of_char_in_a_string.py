my_string = 'India is my Country!!!'
my_string=my_string.split()
print(my_string)
for li in my_string:
    print(len(li))


def ras(my_string1):
    my_string1=my_string1.split()
    for letters in my_string1:
        print(len(letters))

my_string1 = 'India is a '
print(ras(my_string1))