def fun(list1,num):
    print(f"List raised to power of {num} : ",end="")
    return [i**num for i in list1]
print(fun([1,2,3],3))