#pseudocode
'''
step 1:take a list as user input as my_list
step 2:assign sum=0
step 3:create an empty list named unique
step 4:use for loop to get each element from my_list
    if that element not in unique,append it to unique
step 5:print unique
'''

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    elements = (input(f"Enter the index {i} element : "))
    my_list.append(elements)
print("list = ", my_list)


unique = []
for i in my_list:
    if i not in unique:
        unique.append(i)
print("unique list : ", unique)