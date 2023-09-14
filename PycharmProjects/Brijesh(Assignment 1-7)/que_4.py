#pseudocode
'''
step 1:take a list as user input as my_list,sort it and print

step 2:assign sum=0
step 3:use for loop to get each element from my_list
       sum=sum+element for each iteration to get the sum of all elements of the my_list
step 4:mean =sum/number of elements
step 5;print mean

step 6:if remainder of n divided by 2 equals 0,it is even
       for even use n//2 and (n//2)-1 to get middle indices
       use these indices to get corresponding elements and take its avg and print it
step 7:else it is odd
       for odd use n//2 to get middle index
       my_list[n//2] gives the median and print it

step 8:create an empty dictionary named dict_mode
step 9:use for loop to get each element from my_list
       get count of each element and store in dictionary with key as element and value as count
step 10:use for loop to get key and value from dict_mode.values()
        if value equals max of dict_mode.values()    (max count)
        print its key as mode  (max repeated element)

step 11:assign sum=0
step 12:use for loop to get each element from my_list
        sd=square of (element - mean)
        sum=sum+sd gives the sum of this value for each element
step 13:print (sum/number of elements) which gives the standard deviation
'''

n=int(input("Enter number of elements : "))
my_list=[]
for i in range(n):
    elements=int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
    my_list.sort()
print("list = ",my_list)

#mean

sum=0
for i in my_list:
    sum=sum+i
mean=sum/n
print("mean = ",mean)

#median

if n%2==0:
    print("median = ",(my_list[(n)//2]+my_list[(n//2)-1])/2)
else:
    print("median = ",my_list[(n)//2])

#mode

dict_mode={}
for i in my_list:
    count=my_list.count(i)
    dict_mode[i] = count
for i,j in dict_mode.items():
    c=0
    if j == max(dict_mode.values()) and j > 1:
        print("Mode = ",i)
        break
    else:
        c=c+1
if c>0:
    print("Mode = ",0)

#standard deviation

sum=0
for x in my_list:
    sd=(x - mean)**2
    sum=sum+sd
print("standard deviation : ",(sum/n)**(1/2))