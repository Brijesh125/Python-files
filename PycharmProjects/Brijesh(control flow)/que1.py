#Triangle
l1=int(input("Enter the 1st length : "))
l2=int(input("Enter the 2nd length : "))
l3=int(input("Enter the 3rd length : "))
if l1==l2 and l2==l3:
    print("The triangle is Equilateral")
elif l1==l2 or l1==l3 or l2==l3:
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")
