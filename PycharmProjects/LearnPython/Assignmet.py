#Greatest
'''
x=int(input("Enter 1st number : "))
y=int(input("Enter 2nd number : "))
z=int(input("Enter 3rd number : "))
if x > y and x > z:
    print("x = ",x," is the greatest")
elif y > x and y > z:
    print("y = ",y," is the greatest")
elif z > x and z > y:
    print("z = ",z," is the greatest")
else:
    print("invalid")
'''
#Unique elements from list
'''
my_list=[1,2,4,4,1,4,2,6,2,9]
new_list=[]
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print("list of unique elements : ",new_list)
'''
#largest number from list
'''
my_list=[17,3,11,12,8,3,20,5]
largest=my_list[0]
for i in my_list:
    if i > largest :
        largest=i
print("largest number = ",largest)
'''
#power of a number
'''
number=int(input("Enter the number : "))
power=int(input("Enter the power : "))
x=number
for i in range(1,power):
    number=number*x
print("ans = ",number)
'''
#Factorial
'''
x=input("Enter the number : ")
x=[int(i) for i in x]
sum=0
for i in x:
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum=sum+fact
print("ans = ",sum)
'''
#list to dict
'''
keys=["Ten","Twenty","Thirty"]
values=[10,20,30]
ans={}
dict_list=keys+values
for i in range(len(dict_list)):
    if i < len(keys):
        ans[dict_list[i]]=dict_list[i+len(keys)]
ans.update({"Fourty":40,"Fifty":50})
print("Dictionary :",ans)
'''
#Remove vowels
'''
s=input("Enter a string : ")
vowels="aeiou"
for i in s:
    if i not in vowels:
        print(i,end="")
'''
#Dict_set
#1
'''
list_1=[[5,6,7],[8,3,2],[8,2,1]]
dic={}
for i in range(len(list_1)):
    dic[i+1]=list_1[i]
print(dic)
'''
#2
'''
list_2=[1,"a",2,"b",3,"c"]
dic={}
for i in range(0,len(list_2)-1,2):
    dic[list_2[i]]=list_2[i+1]
print(dic)
'''
#3
'''
my_dict = {1: 'apple', 2: 'banana', 3: 'orange'}
my_list=list(my_dict.items())
print(my_list)
'''
#4
'''
dic = {2:"Apple",1:"Mango",3:"Orange",4:"Banana"}
keys=list(dic.keys())
keys.sort()
dict={}
for i in keys:
    for x,y in dic.items():
        if i==x:
            dict[i]=y
print(dict)
'''
#5
'''
n=int(input("Enter the number : "))
mul={}
for i in range(1,n+1):
    mul[i]=i*3
print(mul)
'''
#6
'''
string_1 = "Life of Pie"
vowels=set("aeiouAEIOU")
c=0
l=[]
for i in vowels:
    for j in string_1:
        if i==j:
            c=c+1
            l.append(i)
print("No of vowels :",c)
print(l)
'''
#control flow
#1
"""
l1=int(input("Enter the 1st length : "))
l2=int(input("Enter the 2nd length : "))
l3=int(input("Enter the 3rd length : "))
if l1==l2 and l2==l3:
    print("Equilateral")
elif l1==l2 or l1==l3 or l2==l3:
    print("Isosceles")
else:
    print("Scalene")
"""
#2
"""
#a 

n=int(input("Enter the number of line : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")
print("\n")

#b

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\r")
print("\n")

#c

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("\r")
print("\n")

#d

for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(" ",end=" ")
    for j in range(i,i+i):
        print(j,end=" ")
    for j in range(i+i-1,i,-1):
        print(j-1,end=" ")
    print("\r")
"""
#3
"""
f=int(input("Enter the first number of range : "))
l=int(input("Enter the last number of range : "))
for i in range(f,l+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count=count+1
    if count == 2:
        print(i)
"""
#4
"""
c=int(input("Enter the count : "))
for i in range(c):
    print(i)
for i in range(c,-1,-1):
    print(i)
"""
#5
"""
n=105
while n>7:
    print(n, ",", end="")
    n=n-7
print(n)
"""
#6
"""
f=int(input("Enter the first number of range : "))
l=int(input("Enter the last number of range : "))
while f<=l:
    if f%2==0:
        print(f)
    f+=1
"""
#7
"""
num=int(input("Enter the number : "))
tem=num
sum=0
while(tem!=0):
    rem=tem%10
    cube=rem**3
    sum=sum+cube
    tem=tem//10
if sum==num:
    print(num,"is an Amstrong number")
else:
    print(num,"is not an Amstrong number")
"""
