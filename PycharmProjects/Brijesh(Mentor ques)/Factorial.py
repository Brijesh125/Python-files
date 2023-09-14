#pseudocode
'''
step 1:take number as user input(string)
step 2:assign sum=0
step 3:use for loop to get each element of string
     convert it into int
     fact=1
     step 4:use for loop in range 1 to single number+1
            fact=fact*j to get factorial after the iterations
     step 5:sum=sum+fact to get sum of individual digit's factorial
step 6:print sum
'''

number=input("Enter the number : ")
sum=0
for i in number:
    i=int(i)
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum=sum+fact
print("ans = ",sum)