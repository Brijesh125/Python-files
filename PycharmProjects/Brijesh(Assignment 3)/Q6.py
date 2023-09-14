#Take a number N as input. Print “Power of two” if the number is a power of two (ex. 2, 4, 8, 16. ..) else print “Not a power of two”
def binary(num):
    lis = []
    for i in range(32):
        rem = num % 2
        num = num // 2
        lis.append(rem)
    lis.reverse()
    return lis
N=int(input("Enter the number : "))
binary=binary(N)
print("Binary : ",end="")
for i in binary:
    print(i,end="")
print("\r")
print("Power of two") if binary.count(1)==1 else print("Not a power of two")