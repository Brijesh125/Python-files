#pseudocode
'''
step 1:take a string as user input
step 2:assign all the vowels to a variable
step 3:use for loop to get each element of string
       if that element not in vowels,print that element
'''


s=input("Enter a string : ")
vowels="aeiouAEIOU"
for i in s:
    if i not in vowels:
        print(i,end="")