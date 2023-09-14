#pseudocode
'''
step 1:assign a list as my_list
step 2:create an empty list as new_list
step 3:use for loop to get each element from my_list
       if that element not in new_list,append it to new_list
step 4:print new_list to get unique list
'''

my_list=[1,2,4,4,1,4,2,6,2,9]
new_list=[]
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print("list of unique elements : ",new_list)
