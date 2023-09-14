def decimal(list1):
    list2=[]
    list3=[]
    for i in range(0,len(list1),8):
        list2.append(list1[i:i+8])
    for i in list2:
        sum=0
        for j in range(len(i)):
            sum=sum+i[-j-1]*2**j
        list3.append(sum)
    tuple1=tuple(list3)
    print("tuple1 : ",end=" ")
    return tuple1
list1=[1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
print(decimal(list1))