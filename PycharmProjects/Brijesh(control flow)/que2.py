#patterns
#a

n=int(input("Enter the number of line : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")
print("\n")

#b

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\r")
print("\n")

#c

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("\r")
print("\n")

#d

for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(" ",end=" ")
    for j in range(i,i+i):
        print(j,end=" ")
    for j in range(i+i-1,i,-1):
        print(j-1,end=" ")
    print("\r")