# x = "kamalesh"
# print(x.capitalize())
# print(x.center(50, "*"))
# x=["a","b","c",1,2,3,4]
# print(x)
# print(x.index("c"))
# x.append(9)
# print(x)
# x.insert(2,6)
# print(x)
# print(x.pop(2))
# x.remove(9)
# del x[6]
# print(x)
# x=(1,2,3,"x")
# y=list(x)
# print(x)
# print(y)
# x=tuple(y)
# print(x)
list1=list(input("Enter the 1st list : ").split())
list2=list(input("Enter the 2nd list : ").split())
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print("common list : ",common)