#Take an integer as input. Extract last 4 bits of the integer and print the value.

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
print("last four bits : ",end="")
for i in binary[:4]:
    print(i,end="")
print("\r")
dec=0
for i in range(len(binary[:4])):
    dec=dec+binary[i]*2**(len(binary[:4])-1-i)
print("Decimal value of last four bits = ",dec)