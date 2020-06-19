#It continues to execute a block of code when the conditions remains true

x = 0
while x<5:
    print(f'The value of {x} is less than 5')
    x=x+1


#Continue
my_string='Adipoli'
for letters in my_string:
    if letters=='i':
        continue
    print(letters)


#Break
x=0
while x<5:
    print(f'The value of {x} is less than 5')
    x=x+1
    if x==2:
        break