#pseudocode
'''
step 1:take number and power as user inputs
step 2:store the number in x
step 3:use for loop in range of 1 to power
       number=number*x for each iteration where x is the intial value of number
step 4:print number
'''

number=int(input("Enter the number : "))
power=int(input("Enter the power : "))
x=number
for i in range(1,power):
    number=number*x
print("ans = ",number)