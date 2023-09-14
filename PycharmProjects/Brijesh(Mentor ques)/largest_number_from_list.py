#pseudocode
'''
step 1:assign a list as my_list
step 2:assign 1st element as largest
step 3:use for loop to get each element from my_list
       if that element is greater than largest,replace value in largest with that element
step 4:print largest
'''

my_list=[17,3,11,12,8,3,20,5]
largest=my_list[0]
for i in my_list:
    if i > largest :
        largest=i
print("largest number = ",largest)