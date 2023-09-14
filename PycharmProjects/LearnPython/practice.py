#Assignment 1-7

#1
'''
x=int(input("Enter the 1st number : "))
y=int(input("Enter the 2nd number : "))
if x%y == 0:
    print("True")
else:
    print("False")
'''
#2

"""x1=int(input("Enter the x1 coordinate : "))
y1=int(input("Enter the y1 coordinate : "))
x2=int(input("Enter the x2 coordinate : "))
y2=int(input("Enter the y2 coordinate : "))
tuple_1=(x1,y1)
tuple_2=(x2,y2)
difference=((tuple_2[0]-tuple_1[0]),(tuple_2[1]-tuple_1[1]))
print("tuple 1 : ",tuple_1)
print("tuple 2 : ",tuple_2)
distance=(difference[0]**2 + difference[1]**2)**(1/2)
print("distance = ",distance)
"""
#3
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
'''
#4
"""
n=int(input("Enter number of elements : "))
my_list=[]
sum=0
for i in range(n):
    elements=int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
    my_list.sort()
print("list = ",my_list)
for i in my_list:
    sum=sum+i
mean=sum/n
print("mean = ",mean)
if n%2==0:
    print("median = ",(my_list[(n)//2]+my_list[(n//2)-1])/2)
else:
    print("median = ",my_list[(n)//2])
dict_mode={}
for i in my_list:
    count=my_list.count(i)
    dict_mode[i] = count
for i,j in dict_mode.items():
    if max(dict_mode.values()) <= 1:
        print("Mode = ",my_list)
        break
    else:
        if j == max(dict_mode.values()):
            print("Mode = ", i)
sum=0
for x in my_list:
    sd=(x - mean)**2
    sum=sum+sd
print("standard deviation : ",(sum/n)**(1/2))
"""
#5
'''
decimal=int(input("Enter the number : "))
remainder_list=[]
binary=0
while(decimal!=0):
    remainder=decimal%2
    remainder_list.append(remainder)
    decimal=decimal//2
reverse=remainder_list[::-1]
for i in reverse:
    binary=binary*10+i
print("binary :",binary)
'''
#6
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
'''
#7
"""
n=int(input("Enter number of elements : "))
my_list=[]
sum=0
for i in range(n):
    elements=(input(f"Enter the index {i} element : "))
    my_list.append(elements)
print("list = ",my_list)
unique=[]
for i in my_list:
    if i not in unique:
        unique.append(i)
print("unique list : ",unique)
"""
#8
"""
file_name=input("Enter the file name : ") #dict1.csv
                                          #dict2.csv
                                          #dict3.csv
f=open(file_name,'r')
dic={}
for i in f:
    items=i.strip().split(",")
    for i in range(2):
        if items[i].isnumeric():
            items[i]=int(items[i])
    dic[items[0]]=items[1]
print("Dictionary : ",dic)
f.close()"""
# import csv
# dic = {}
# with open('Book1.csv', 'r') as file:
#     read = csv.reader(file)
#     for i in read:
#         dic[i[0]] = i[1]
# print(dic)


#9
"""
file_name=input("Enter the file name : ") #matrix1.csv
                                          #matrix2.csv
                                          #matrix3.csv
f=open(file_name,'r')
matrix=[]
transpose=[]
for i in f:
    row=i.strip().split(",")
    for j in range(len(row)):
        if row[j].isnumeric():
            row[j]=int(row[j])
    matrix.append(row)
print("matrix : ",matrix)
for i in range(len(matrix[0])):
    matrix2 = []
    for j in range(len(matrix)):
        matrix2.append(matrix[j][i])
    transpose.append(matrix2)
print("transpose : ",transpose)
f.close()
"""
# import csv
# dic = {}
# matrix=[]
# transpose=[]
# with open('Book2.csv', 'r') as file:
#     read = csv.reader(file)
#     for i in read:
#         matrix.append(i)
# print("matrix : ",matrix)
# for i in range(len(matrix)):
#     matrix2 = []
#     for j in range(len(matrix)):
#         matrix2.append(matrix[j][i])
#     transpose.append(matrix2)
# print("transpose : ",transpose)

#10
"""
lis=[]
dic={}
file_name=input("Enter the file name : ") #role.csv
file=open(file_name,'r')
for i in file:
    row=i.strip().split(",")
    if '' in row:
        for j in range(row.count('')):
            row.remove('')
    lis.append(row)
for i in lis:
    dic[i.pop(0)]=i
print("Dictionary of data : ",dic)
name=input("Enter the name:")
if name not in dic:
    print("invalid user name")
else:
    role = input("Enter the role:")
    if role in dic[name]:
        print("True")
    else:
        print("False")
file.close()
"""


#Assignment 8-9


#1
"""
n=int(input("Enter number of elements : "))
my_list=[]
for i in range(n):
    elements=int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
print("list = ",my_list)


for i in range(n):
    for j in range(i+1,n):
        if my_list[i] > my_list[j]:
            my_list[i],my_list[j]=my_list[j],my_list[i]
print("sorted list = ",my_list)
target=int(input("Enter the target : "))
start=0
stop=len(my_list)-1
while start<=stop:
    mid = (start+stop) // 2
    if target==my_list[mid]:
        print("index of target : ",mid)
        break
    elif target<my_list[mid]:
        stop=mid-1
    else:
        start=mid+1


if target not in my_list:
    if stop < 0:
        print(0)
    elif start >= len(my_list):
        print(len(my_list) - 1)
    elif abs(target - my_list[start]) < abs(target - my_list[stop]):
        print("index of closest number : ", start)
    else:
        print("index of closest number : ", stop)
"""
#2
"""
string=input("Enter the string : ")
ascii={}
list_ascii=[]
for i in range(256):
    ascii[i]=chr(i)
print("dict of ascii : ",ascii)
for s in string:
    for i,j in ascii.items():
        if s==j:
            list_ascii.append(i)
print("list of ascii : ",list_ascii)
"""
#5
"""
n=int(input("Enter the number of strings : "))
string=""
for i in range(1,n+1):
    ip_string=input(f"Enter the string {i} : ")
    if i==1:
        string=string+ip_string
    else:
        string=string+","+ip_string
print("output :",'"'+string+'"')
"""

#6
"""
separator=input("Enter the separator string : ")
n=int(input("Enter the number of strings : "))
string=""
for i in range(1,n+1):
    ip_string=input(f"Enter the string {i} : ")
    if i==1:
        string=string+ip_string
    else:
        string=string+separator+ip_string
print("output :",'"'+string+'"')
"""

