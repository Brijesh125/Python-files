#Take two integers as inputs. Replace bits 8 to 15 of first input with bits 8 to 15 from second input and print the result.

def binary(num):
    lis = []
    for i in range(32):
        rem = num % 2
        num = num // 2
        lis.append(rem)
    lis.reverse()
    return lis
num1=int(input("Enter the 1st number : "))
num2=int(input("Enter the 2nd number : "))
binary1=binary(num1)
binary2=binary(num2)
print("Binary of num1: ",end="")
for i in binary1:
    print(i,end="")
print("\r")
print("Binary of num2 : ",end="")
for i in binary2:
    print(i,end="")
print("\r")
print("result : ",end="")
result=binary1[:-16]+binary2[-16:-8]+binary1[-8:]
for i in result:
    print(i,end="")