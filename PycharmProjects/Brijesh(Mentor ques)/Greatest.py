#pseudocode
'''
step 1:take x,y and z as user input
step 2:if x is greater than both y and z,print x = (values) is greatest
step 3:elif y is greater than both x and z,print y = (values) is greatest
step 4:elif z is greater than both x and y,print z = (values) is greatest
step 5:else print invalid
'''

x=int(input("Enter 1st number : "))
y=int(input("Enter 2nd number : "))
z=int(input("Enter 3rd number : "))
if x > y and x > z:
    print("x = ",x," is the greatest")
elif y > x and y > z:
    print("y = ",y," is the greatest")
elif z > x and z > y:
    print("z = ",z," is the greatest")
else:
    print("invalid")
