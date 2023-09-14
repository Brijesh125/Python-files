#Write a program that takes an integer (N) and another integer (P). Print the bit at position P in the integer N.

def binary(num):
    lis = []
    for i in range(32):
        rem = num % 2
        num = num // 2
        lis.append(rem)
    lis.reverse()
    return lis
N=int(input("Enter the 1st number : "))
P=int(input("Enter the 2nd number : "))
binary=binary(N)
print("Binary of num1: ",end="")
for i in binary:
    print(i,end="")
print("\r")
print(f"bit at position {P} :",binary[-P-1])