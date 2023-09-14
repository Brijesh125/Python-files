#prime
f=int(input("Enter the first number of range : "))
l=int(input("Enter the last number of range : "))
prime=[]
for i in range(f,l+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count=count+1
    if count == 2:
        prime.append(i)
print("prime numbers are : ",prime)

