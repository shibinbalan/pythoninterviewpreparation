def rem_dup(my_string):
    return "".join(set(my_string))


my_string = 'India is my country!!!'
print(rem_dup(my_string))