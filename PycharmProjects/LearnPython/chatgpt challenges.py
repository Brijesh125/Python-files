#1
# Write a Python function that takes two lists of integers as input and returns a list containing all pairs of integers, one from each list, where the sum of the pair is a prime number.
"""
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return i
    else:
        pass
def challenge1(l1,l2):
    l3=[]
    for i in l1:
        for j in l2:
            if (i + j) == prime((i + j)):
                l3.append((i, j))
    return(l3)
l1=[1,2,3]
l2=[4,5,6]
print(challenge1(l1,l2))
"""

# def prime(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:c=c+1
#     if c==2:return i
# def challenge1(l1,l2):
#     return [(i,j) for j in l2 for i in l1 if (i+j) == prime(i+j)]
# print(challenge1([1,2,3],[4,5,6]))

#2
# Write a program that takes in a list of integers and returns the maximum sum of any contiguous subarray of the given list.
"""
def challenge2(l1):
    sum,d=[],{}
    for i in range(len(l1)+1):
        for j in range(len(l1)+1):
            s=0
            l2=l1[i:j]
            for k in l2:
                s=s+k
                sum.append(s)
                d[s]=l2
    for i,j in d.items():
        if i==max(sum):
            return j
l1=[1,-2,3,4,-5,8]
print(challenge2(l1))
"""
#3
# Write a program that takes in a list of integers and returns the maximum product that can be obtained from any three integers in the list. The list may contain both positive and negative integers.
# l1=[1, -10, -10, 5, 5]
# l2=[]
# for i in l1:
#     if i < 0:
#         l2.append(i)
# max1=max(l1)
# if len(l2) > 1:
#     min2 = min(l1)
#     if l1.count(min2) == 2:
#         min3 = min2
#     else:
#         l1.remove(min2)
#         min3 = min(l1)
#     m1=max1*min2*min3
# if l1.count(max1) == 3:
#     max2 = max1
#     max3 = max1
# elif l1.count(max1) == 2:
#     max2 = max1
#     l1.remove(max1)
#     max3 = max(l1)
# else:
#     l1.remove(max1)
#     max2 = max(l1)
#     if l1.count(max2) == 2:
#          max3 = max2
#     else:
#         l1.remove(max2)
#         max3 = max(l1)
# m2=max1*max2*max3
# if m1>m2:
#     print(m1)
# else:
#     print(m2)
"""
def challenge3(l1):
    l1.sort()
    p1 = 1
    for i in range(-1, -4, -1):
        p1 = p1 * l1[i]
    l1.sort()
    p2 = l1[-1] * l1[0] * l1[1]
    if p1>p2:
        return p1
    else:
        return p2

l1=[1,-10,-10,4,5]
print(challenge3(l1))
"""
"""
def challenge3(l1,num):
    l=[]
    import itertools
    for i in itertools.combinations(l1,num):
        p=1
        for j in range(len(i)):
            p=p*i[j]
        l.append(p)
    return max(l)
l1=[1,-10,-10,4,5,-1]
print(challenge3(l1,4))
"""
#4
# Write a function named find_largest_subarray_sum that takes a list of integers as input, and returns the largest sum that can be obtained by summing up a subarray of the input list.
"""
def challenge4(l1):
    sum,d=[],{}
    for i in range(len(l1)+1):
        for j in range(len(l1)+1):
            s=0
            l2=l1[i:j]
            for k in l2:
                s=s+k
                sum.append(s)
                d[s]=l2
    for i,j in d.items():
        if i==max(sum):
            return i
l1=[1,-2,3,10,-4,7,2,-5]
l2=[1,2,7,-4,3,2,-10,9,1]
print(challenge4(l1))
"""
#5
# Write a Python function that takes in a list of integers and returns the two numbers that add up to a specific target. You cannot use the same element twice and the function should return the indices of the two numbers in the list.
"""
def challenge5(lis,target):
    for i in lis:
        for j in lis:
            if i+j==target:
                print((lis.index(i),lis.index(j)))
                lis[lis.index(i)]=0
                lis[lis.index(j)]=0
challenge5([1,2,3,4,5],7)
"""
#6
# Write a Python function that takes in a list of integers and returns the length of the longest subarray where the sum of the subarray is less than or equal to a given target. The subarray should contain at least one element.
"""
def challenge6(lis,target):
    length=[]
    for i in range(len(lis)+1):
        for j in range(i+2,len(lis)+1):
            l1=lis[i:j]
            if sum(l1)<=target:
                length.append(len(l1))
    return max(length)
print(challenge6([1,2,3,4,5],7))
"""
#7
# Write a Python program to generate all possible combinations of n items taken k at a time. The input n and k are integers where 0 <= k <= n. You cannot use the built-in itertools library for this question.
"""
def challenge7(n,k):
    import itertools
    for x in itertools.combinations(range(1,n+1),k):
        print(list(x))
challenge7(5,3)
"""
#8
# Write a Python function that takes in a list of integers and returns the longest subarray with a sum that is divisible by a given integer k.
"""
def challenge8(lis,target):
    dic1={}
    for i in range(len(lis)+1):
        for j in range(i+2,len(lis)+1):
            l1=lis[i:j]
            if sum(l1)%target==0:
                dic1[len(l1)]=l1
    for i,j in dic1.items():
        if i==max(dic1.keys()):
            return j
print(challenge8([3,1,2,10,4,7],8))
"""
#9
# Write a Python function that takes a string as input and returns the longest substring that contains at most two distinct characters.
"""
def challenge9(s):
    distinct = []
    string = [[s[i:j] for j in range(1, len(s) + 1) if i < j] for i in range(len(s))]
    for i in string:
        for j in i:
            distinct.append(j) if len(set(j)) <= 2 else None
    length = {i: len(i) for i in distinct}
    for i, j in length.items():
        if j == max(length.values()):
            return i

s = "abcbbbbcccbdddadacb"
print(challenge9(s))
"""
#10
# Write a Python function to find the first non-repeating character in a given string.
"""
def challenge10(s):
    d = {i: s.count(i) for i in s}
    for i, j in d.items():
        if j == 1:
            return i
s="abacabad"
print(challenge10(s))
"""

hour=int(input("Enter the hour : "))
min=int(input("Enter the minute : "))
if hour in range(1,13) and min in range(0,60):
    hour_angle=0
    min_angle=0
    if min in range(0,10):
        print(f"Time is {hour}:0{min}")
    else:print(f"Time is {hour}:{min}")
    for i in range(0,hour):
        hour_angle=hour_angle+30
    for i in range(0,min):
        hour_angle=hour_angle+.5
        min_angle=min_angle+6
    print("angle is ",abs(hour_angle-min_angle))

else:
    print("Invalid entry")