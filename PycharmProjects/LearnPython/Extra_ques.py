#Amstrong
'''
num=int(input("Enter the number : "))
tem=num
sum=0
while(tem!=0):
    rem=tem%10
    cube=rem**3
    sum=sum+cube
    tem=tem//10
if sum==num:
    print("Amstrong")
else:
    print("Not Amstrong")
'''
#Even and positive
'''
n=int(input("Enter number of elements : "))
my_list=[]
new_list=[]
for i in range(n):
    elements=int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
print("list = ",my_list)
for i in my_list:
    if i%2==0 and i>0:
        new_list.append(i)
print("New list = ",new_list)
'''
#pattern 1
'''
n=65
for i in range(1,6):
    for j in range(1,i+1):
        c=chr(n)
        n=n+1
        print(c,end=" ")
    print("\r")
'''
#patten 2
'''
s=1
for i in range(5,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,s+1):
        print(k,end=" ")
    s=s+2
    print("\r")
'''
#pattern 3
"""
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print("\r")
"""
#pattern 4(diamond)
'''
s=1
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(' ',end=" ")
    for k in range(1,s+1):
        print("*",end=" ")
    s=s+2
    print("\r")
s=s-4
for i in range(1,5):
    for j in range(1,i+2):
        print(' ',end=" ")
    for k in range(1,s+1):
        print("*",end=" ")
    s=s-2
    print("\r")
'''
#pattern 5 (Holo)
'''
s=1
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(' ',end=" ")
    for k in range(1,s+1):
        if k==1 or k==s:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    s=s+2
    print("\r")
s=s-4
for i in range(1,5):
    for j in range(1,i+2):
        print(' ',end=" ")
    for k in range(1,s+1):
        if k == 1 or k == s:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    s=s-2
    print("\r")
'''
#Diamond
"""
n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(" "*(n+1-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n+1-i)+"* "*i)
"""
#Holo daimond
"""
n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(" "*(n+1-i)+"* "+"  "*(i-2)+"* " if i>1 else " "*n+"*")
for i in range(n-1,0,-1):
    print(" "*(n+1-i)+"* "+"  "*(i-2)+"* " if i>1 else " "*n+"*")
"""
#prime
'''
n=int(input("Enter the last number of range : "))
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count=count+1
    if count == 2:
        print(i)
'''
#leap year
'''
year=int(input("Enter the year : "))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("not a leap year")
else:
    if year % 4 == 0:
        print("leap year")
    else:
        print("not a leap year")
'''
#uncommon
'''
s1="apple banana mango"
s1=s1.split()
s2="mango orange apple"
s2=s2.split()
new_list=[]
for i in s1:
    if i not in s2:
        new_list.append(i)
for i in s2:
    if i not in s1:
        new_list.append(i)
print(new_list)
'''
#sorting
"""
n=int(input("Enter number of elements : "))
my_list=[]
for i in range(n):
    elements=int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
print("list = ",my_list)
for i in range(n):
    for j in range(i,n):
        if my_list[i] > my_list[j]:
            my_list[i],my_list[j]=my_list[j],my_list[i]
print("sorted list : ",my_list)
"""
#Exchange keys and values
'''
a={"Hello": "world", 1:2}
b={"zara":"john","trisha":"sruthi"}
c={}
a.update(b)
print(a)
for i,j in a.items():
    c[j]=i
print(c)
'''
#mark_dict
'''
a=(30,40,10,20)
a=list(a)
a.sort()
b=[]
d={}
for i in range(len(a)):
    d[f"mark{i+1}"]=a[i]
print(d)
'''
#reverse int
'''
a=12345
while a!=0:
    r=a%10
    print(r,end="")
    a=a//10
'''
'''
a=12345
a=str(a)
b=a[::-1]
b=int(b)
print(b)
'''
#change an element
'''
a=[0,10,20,30,20,10]
for i in range(len(a)):
    if a[i]==20:
        a[i]=200
        break
print(a)
'''
#Middle 3
'''
x=input("Enter the string :")
print(x[(len(x)//2)-1:(len(x)//2)+2])
'''
#uncommon str
'''
s1="abcs"
s2="cxzca"
s3=(set(s1)-set(s2))|(set(s2)-set(s1))
for i in s3:
    print(i,end="")
print("\r")
for i in s1:
    if i not in s2:
        print(i,end="")
for i in s2:
    if i not in s1:
        print(i,end="")
'''
#perfect square
'''
a=0
n=int(input("Enter the number : "))
for i in range(n+1):
    if i*i==n:
        a=i
print("perfect") if a*a==n else print("not perfect")
'''
#interchange keys and values
'''
dic={"Rasgulla":"IND","Pavlova":"AUS","ladoo":"IND","Apple Pie":"USA","pie":"USA","halwa":"IND"}
new_dic={}
for i,j in dic.items():
    if j not in new_dic:
        new_dic[j]=i
    else:
        if isinstance(new_dic[j],list):
            new_dic[j].append(i)
        else:
            new_dic[j]=[new_dic[j],i]
print(new_dic)
'''
#2 lists to same index list
'''
list1 = ["M", "na", "i", "ano"]
list2 = ["y", "me", "s", "ra"]
list3=[]
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)
'''
#sum of square of sum(nested list)
'''
sum=0
l=[[1,5,6],[5,6,9],[4,-8,9],[7,4,3]]
for i in range(len(l)):
    s = 0
    for j in range(len(l)-1):
        s=s+l[i][j]
    sq=s*s
    sum=sum+sq
print(sum)
'''
#sum of values
'''
s=0
d={'a':100,'b':200,'c':300}
for i in d.values():
    s=s+i
print(s)    
'''
#nested list
'''
l1=[1,2,3]
l2=[]
for i in l1:
    j=i**3
    l2.append([i,j])
print(l2)
'''
#letter and number
'''
s = input("Enter a string: ")
x = 2
y = 3
for i in s:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        x = True
    elif i >= '0' and i <= '9':
        y = True
if x==y:
    print("True")
else:
    print("False")
'''
#palindrome
'''
s = input("Enter a string: ")
x=s[::-1]
if s==x:
    print("palindrome")
else:
    print("Not palindrome")
'''
#Divisible by 3
'''
for i in range(1,11):
    if i%3 == 0:
        print("A number divisible by 3")
    else:
        print(i)
'''
#sum of i and i-1th term
"""
l=[1,5,8,3,1]
for i in range(len(l)):
    print(l[i]+l[i-1])
"""
#sum of a element to dict
"""
l=[124,34,78,89]
d={}
for i in l:
    x=i
    s=0
    while x>0:
        r=x%10
        s=s+r
        x=x//10
    d[i]=s
print(d)
"""
#tuple divisible by 6
"""
l=[(34,2,45,6),(990,12,32,31),(6,12,18,24),(30,66,72,84)]
for i in l:
    c = 0
    for j in i:
        if j%6==0:
            c=c+1
    if c==len(i):
        print(i)
"""
#sum=given value
"""
v=int(input("Enter the value:"))
l=[1,2,4,5,8,74,1,5,1,54,16,451,6,564,54,515,45,458,420,23,8,51,20056,10]
l2=[]
for i in l:
    for j in l:
        if i+j==v:
            k=[i,j]
            if k not in l2:
                l2.append(k)
print(l2)
"""
#union and intersection
"""
l1=[1,4,3,2,6]
l2=[2,5,7,3,2]
l3,l4=[],[]
for i in (l1+l2):
    if i not in l3:
        l3.append(i)
l3.sort()
print(l3)
for i in l1:
    if i in l2:
        l4.append(i)
l4.sort()
print(l4)
"""
#lcm
"""
l1=[]
l2=[]
c=[]
for i in range(1,11):
    l1.append(4*i)
    l2.append(5*i)
for i in l1:
    if i in l2:
        c.append(i)
print(min(c))
"""









