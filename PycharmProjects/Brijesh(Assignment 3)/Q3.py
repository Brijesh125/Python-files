# Take an integer as an input. Extract bits in position 7 to 15 and print the value.

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
print("7 to 15 bits : ",end="")
for i in binary[-16:-7]:
    print(i,end="")
print("\r")
dec=0
for i in range(len(binary[-16:-7])):
    dec=dec+binary[-16+i]*2**(len(binary[-16:-7])-1-i)
print("Decimal value of 7 t0 15 bits = ",dec)