#pseudocode
'''
step 1:take the decimal number as user input
step 2:create an empty list as remainder_list
step 4:while loop run til decimal not equal to 0
       inside while loop :
       divide decimal by 2 and append the remainder to the remainder_list
       divide decimal by 2 using flow division (//) to get int only
       repeat the loop til decimal=0
step 5:reverse the remainder_list using slicing and store in reverse
step 6:use for loop to get each element from reverse list
step 7:print each element in a line using end
'''

decimal=int(input("Enter the number : "))
remainder_list=[]
while(decimal!=0):
    remainder_list.append(decimal%2)
    decimal=decimal//2
reverse=remainder_list[::-1]
print("Binary =",end=" ")
for i in reverse:
    print(i,end="")