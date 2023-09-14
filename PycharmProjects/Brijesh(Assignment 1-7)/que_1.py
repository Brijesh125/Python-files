#pseudocode
'''
step 1:take 1st number as user input  and store in x
step 2:take 2nd number as user input and store in y
step 3:if x%y==0(divide x by y and check remainder == 0) then print True
step 4:else print false
'''

x=int(input("Enter the 1st number : "))
y=int(input("Enter the 2nd number : "))
if x%y == 0:
    print("True")
else:
    print("False")