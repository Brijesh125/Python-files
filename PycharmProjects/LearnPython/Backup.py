#Data types
'''
x=1
y=1.5
z=1.5e3
c=1+7j
print(z)
print(type(x))
print(type(y))
print(type(z))
print(type(c))
print(bool())
print(bool(1))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))
print(10<100)
'''
#string
'''
x="Hi,i am Brijesh"
print(len(x))
print("HI" in x)
print("Hello" not in x)
print(x[8:15])
x="Brijesh"
y="Babu"
print(x+" k "+y)
print(f"Hi,i am {x} k {y}")
print(x.upper())
print(x.startswith("B"))
'''
#List
'''
x=["a","b","c",1,2,3,4]
print(len(x))
y=list((9,8,7))
print(x+y)
y[2]=3
print(y)
print(x[2:4])
x.append(9)
print(x)
x.insert(2,6)
print(x)
print(x.index("c"))
print(x.pop(2))
x.remove(9)
del x[6]
print(x)
x.clear()
print(x)
y.sort()
print(y)
z=y.copy()
print(z)
print(z.count(3))
z.extend(y)
print(z)
z.reverse()
print(z)
'''
#Tuple
'''
t=("a","b","c")
(x,y,z)=t
print(x)
print(y)
print(z)
print(t*3)
for i in t:
    print(i)
'''
#Range
'''
x=list(range(5,10,2))
print(x)
x=list(range(5,10))
print(x)
x=list(range(10))
print(x)
for i in x:
    print(i)
'''
#Dictionary
'''
x={"Brand":"Ford","Model 1":"Mustang","Year":2001}
print(x["Model 1"])
x["Model 2"]="challenger"
print(x)
print(x.pop("Model 2"))
x.update({"Model 2":"challenger"})
print(x)
for i in x:
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
print(x.get("Brand","invalid"))
print(x.get("Brand 2","invalid"))
print(x.items())
print(x.keys())
del x["Year"]
print(x)
'''
#Set
'''
x={2,10,50,3,20,90}
x.add(45)
x.remove(90)
print(x)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
'''
#File I/O
'''
f=open("demo.txt",'w')
f.close
'''
'''
f=open("demo.txt",'r')
for aLine in f:
    c=f.readline()
    print(c)
f.close()
'''
'''
f=open("demo.txt",'a')
f.write("\t")
f.write("Fire")
f.close()
'''
#Function
'''
def add(a,b):
    return a+b
x=int(input("Enter x ="))
y=int(input("Enter y ="))
print(add(x,y))
def ad(a,b):
    print(a+b)
ad(x,y)
'''
'''
def c(country="Norway"):
    print("i am from "+country)
c("india")
c()
def f(c3,c2,c1):
    print("c is "+c3)
f(c1="a",c2="b",c3="c")
def g(*c):
    print("c is "+c[2])
g("a","b","c")
def h(**c):
    print("c is "+c["c3"])
h(c1="a",c2="b",c3="c")
'''
#IF
'''
a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))
if a>b:
    print("a is Greater")
elif a==b:
    print("Equal")
else:
    print("b is Greater")
print("sum =",a+b)
if a<b:
    pass
'''
#For
'''
for i in range(11):
    print(i)
    if i==5:
        break
x=["a","b","c"]
y=""
for i in x:
    y=y+" "+i
else:
    print("done")
print(y)
for i in range(11):
    if i==5:
        continue
    print(i)
'''
#While
'''
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
else:
    print("End")
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
'''
#variable scope
'''
x=20 #Global
def f():
    x=10 #local
    global y
    y=30
    print(x)
f()
print(x)
print(y)
'''
#Function as variable
'''
def even(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
x=even
x(9)
x(10)
'''
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def choose(f1,f2,which,a,b):
    if which == "add":
        return f1(a,b)
    else:
        return f2(a,b)
print(choose(add,sub,"add",1,2))
print(choose(add,sub,"sub",1,2))
'''
'''
def add(a,b):
    return a+b
def square(c):
    return c*c
print(square(add(1,9)))
'''
#lambda
'''
x=lambda a,b,c:a+b+c
print(x(1,2,3))
def f(a):
    return lambda b:a+b
x=f(5)
print(x(10))
'''
#map
'''
def sq(a):
    return a*a
l=[1,2,3,4]
m=list(map(sq,l))
print(m)
m1=list(map(lambda a:a*a,l))
print(m1)
l1=[]
for i in l:
    l1.append(i*i)
print(l1)
'''
#Filter
'''
x=list(range(10))
y=list(filter(lambda x:x>3,x))
print(y)
'''
#Reduce
'''
from functools import reduce
def fact(n):
    return reduce(lambda a,b: a*b,list(range(1,n+1)))
print(fact(5))
'''
#zip
'''
x=["a","b","c"]
y=["x","y","z"]
z=list(zip(x,y))
print(z)
'''
#list comprehension
'''
x=list(range(10))
y1=[i*i for i in x]
print(y1)
y2=[i*i for i in x if i<5]
print(y2)
y3=[1 if i>5 else 0 for i in x]
print(y3)
a=["pa","h","po","k","pg"]
b=[i for i in a if "p" in i]
print(b)'''
#Set comprehension
'''
x={1,4,7,9,3}
y={9,1,4,6,7}
z={i for i in x if i in y}
print(z)
'''