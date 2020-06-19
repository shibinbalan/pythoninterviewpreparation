def fibonaci(n):
    if n<1:
        print(n,"Invlid Input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)