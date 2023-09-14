# Take in a user input as integer. Flip the bit at position 11 and print the result.

def binary(num):
    lis = []
    for i in range(32):
        rem = num % 2
        num = num // 2
        lis.append(rem)
    lis.reverse()
    return lis
num=int(input("Enter the number : "))
binary=binary(num)
print("Binary : ",end="")
for i in binary:
    print(i,end="")
print("\r")
binary[-12]=1 if binary[-12]==0 else 0
print("flipped binary : ",end="")
for i in binary:
    print(i,end="")