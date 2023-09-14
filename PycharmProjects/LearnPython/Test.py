"""
a="BOOK"
ch="O"

def fun(a,ch):
    for i in range(len(a)):
        if a[i]==ch:
            return i
def odd_even():
    i=fun(a,ch)
    if i%2==0:
        print("Even")
    else:
        print("Odd")
    for j in range(10):
        print(i)
        i=i+2
odd_even()
"""

w1="she is seven"
w2="car is green"
"""
def same_length(w1,w2):
    l1=w1.split()
    l2=w2.split()
    len1=[len(i) for i in l1]
    len2=[len(i) for i in l2]
    c=0
    for i in range(len(l1)):
       if len1[i]==len2[i]:
           c=c+1
    if c==len(l1):
        return True
    else:
        return False
print(same_length(w1,w2))
"""
# def same_length(w1,w2):
#     len1 = [len(i) for i in w1.split()]
#     len2 = [len(i) for i in w2.split()]
#     return len1==len2
# print(same_length(w1,w2))

def fun(a,ch):
    for i in range(len(a)):
        if a[i]==ch:
            return i
def odd_even():
    i=fun(a,ch)
    try:
        if i == 0:
            print(f"index of {ch} = {i} is neither odd nor even")
        else:
            if i % 2 == 0:
                n="Even"
                print(f"index of {ch} = {i} is {n}")
            else:
                n="Odd"
                print(f"index of {ch} = {i} is {n}")
            print(f"Ten {n} numbers starting from {ch} are : ",end="")
            for j in range(9):
                print(i,end=",")
                i = i + 2
            print(i)
    except:
        print("invalid entry")

a="BRIJESH"
ch="H"
odd_even()