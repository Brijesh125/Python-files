#pseudocode
'''
step 1:take list1 and list 2 as user input and print them
step 2:create an empty list named common
step 3:use for loop to get each element from list1
       if that element in list2,append it to common
step 4:create an empty list named common_list
step 5:use for loop to get each element from common
       if that element not in common_list,append it to common_list(to remove repeated elements)
step 6:print common_list
'''

n1=int(input("Enter number of elements of list1 : "))
list1=[]
for i in range(n1):
    elements=int(input(f"Enter the index {i} element of list1 : "))
    list1.append(elements)
print("list1 = ",list1)
n2=int(input("Enter number of elements of list2 : "))
list2=[]
for i in range(n2):
    elements=int(input(f"Enter the index {i} element of list2: "))
    list2.append(elements)
print("list2 = ",list2)


common=[]
for i in list1:
    if i in list2:
        common.append(i)
common_list=[]
for i in common:
    if i not in common_list:
        common_list.append(i)
print("common list : ",common_list)