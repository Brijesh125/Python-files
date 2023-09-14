#Even numbers in a range
f=int(input("Enter the first number of range : "))
l=int(input("Enter the last number of range : "))
while f<=l:
    if f%2==0:
        print(f)
    f+=1