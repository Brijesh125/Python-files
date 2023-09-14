x=[1,2,3,4,5,6,7,8]
print(x[-2::-3])
print("sam i\nam".split())
print("sam i am".strip())
print(",".join("sam i am"))
print("".join(["sam","i","am"]))
v=bool(None)
print(v)
print(type(v))
x="hell"
y="fire"
s=x+" "+y
print(s)
print(len(s))
print("fire" in s)
print(s[-1::-1])
print(f"{x}! This is {y}")
print(x+"! This is "+y)
print(100>1000)
a=100
b=100
if a>b:
    print("a is G")
elif a==b:
    print("E")
else:
    print("b is G")
f=("a","b","c")
(x,y,z)=f
print(x)
print(y)
print(z)
x=["a","b","c"]
y=["x","y","z"]
z=list(zip(x,y))
print(z)
from functools import reduce
def fact(n):
    return (reduce(lambda a,b: (a)*(b),list(range(1,n+1))))
print(fact(7))
import math as m
print(m.sqrt(4))
print(m.factorial(5))