def main():
    lis = []
    for i in range(5):
        e = int(input(f"Enter {i} index element : "))
        if e<0:
            return f"Invalid entry:{e} is a negative number"
        if e>15:
            return f"Invalid entry:{e} is greater than 15"
        lis.append(e)
    target = int(input("Enter the target : "))
    return binary(lis,target)
def binary(lis,target):
    remainder_list=[]
    if target in lis:
        while target!=0:
            remainder=target%2
            remainder_list.append(remainder)
            target=target//2
        reverse=remainder_list[::-1]
        print("Binary : ", end="")
        return reverse
    return "Target not in list"
print(main())
# list1=[]
# lis=[]
# for i in range(5):
#     e=int(input(f"Enter {i} index element : "))
#     list1.append(e)
# target=int(input("Enter the target : "))
# for i in list1:
#     if i<0:
#         print(f"Error:{i} is a negative number")
#     elif i>15:
#         print(f"Error:{i} is greater than 15")
#     else:lis.append(i)
# def fun(lis,target):
#     remainder_list=[]
#     if target in lis:
#         while target!=0:
#             remainder=target%2
#             remainder_list.append(remainder)
#             target=target//2
#             reverse=remainder_list[::-1]
#         return reverse
#     else:
#         return "Target not in list"
# if len(lis)==len(list1):
#     print("Binary of target : ",fun(lis,target))

