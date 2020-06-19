num=3
if num>1:
    for i in range(2,num):
        if num%i ==0:
            print(num,"its not a prime number!!!")
            break
    else:
        print(num,"its a prime Number!!!")
else:
    print(num,"its not a prime number")
