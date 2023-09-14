def C_to_F(C):
    x=lambda x:(x*9/5)+32
    print("List of fahrenheit : ",end="")
    return [x(i) for i in C]
C=[0,10,21,30,37,40,100,180]
print(C_to_F(C))