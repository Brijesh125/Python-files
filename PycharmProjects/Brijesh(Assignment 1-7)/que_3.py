#pseudocode
'''
step 1:take length of list as user input and store in n
step 2:create an empty list called my_list
step 3:use for loop in range of n to take each element as user input where i corresponds to each index
       during each iteration,append each element to the empty list
step 4:print my_list
step 5:use for loop to get each element from my_list
step 6:if element is less than 10,print the element
'''

n=int(input("Enter number of elements : "))
my_list=[]
for i in range(n):
    elements=int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
print("list = ",my_list)
print("Numbers below 10 are :")
for i in my_list:
    if i < 10:
        print(i)