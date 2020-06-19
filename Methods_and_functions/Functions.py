def myname(name='Shibin'):
    """
    This is Doc String!!!!
    :param name:
    :return:
    """
    print(name)


print(myname('Diljith'))

#Add Function:
def add(n1,n2):
    return n1+n2

koi = add(20,30)
print(koi)

#find out the word "dog" in a string

def dog(my_string):
    return "dog" in my_string.lower()

print(dog("I ama Dog"))


#Pig Latin Problem:
def vowel(my_string):
    if my_string[0] in 'aeiou':
        return my_string + 'ay'
    else:
        return my_string[1:] + 'ay'


print(vowel("apple"))