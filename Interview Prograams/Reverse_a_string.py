# Reverse a string:

def rev_a_str(my_string):
        return my_string[::-1]

my_string='India is my country!!!'
print(rev_a_str(my_string))

#reverse a string without slicing:

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

s= "poda patti!!!"
print(reverse(s))