"""
l=[("y",4),("r",3),("b",2),("y",1)]
d={l[i][1]:l[i][0] for i in range(len(l))}
d1={}
for i,j in d.items():
    if j not in d1:
        d1[j]=[i]
    else:
        d1[j]=d1[j]+[i]
print(d1)
"""


"""
d1={'a':1,'b':2}
d2={'a':2,'c':3}
d3={}
for i in d1:
    if i in d2:
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]
for i in d2:
    if i not in d3:
        d3[i]=d2[i]
print(d3)
"""


# matrix=[[2,7,6],[9,5,1],[4,3,8]]
# sum_row=[]
# sum_coloumn=[]
# sum_dia=[]
# for i in range(len(matrix)):
#     sum1=sum2=0
#     for j in range(len(matrix[0])):
#         sum1=sum1+matrix[i][j]
#         sum2=sum2+matrix[j][i]
#     sum_row.append(sum1)
#     sum_coloumn.append(sum2)
# sum3=sum4=0
# for i in range(len(matrix)):
#     sum3=sum3+matrix[i][i]
#     sum4=sum4+matrix[i][-i-1]
# sum_dia.append(sum3)
# sum_dia.append(sum4)
# sum_dia.append(sum3)
# if sum_row==sum_coloumn and sum_row==sum_dia:
#     print(f"it is a magic square matrix with magic sum {sum3}")
# else:
#     print("not a magic matrix")


# def fun(matrix):
#     sum_row = []
#     sum_coloumn = []
#     for i in range(len(matrix)):
#         sum1 = sum2 = 0
#         for j in range(len(matrix[0])):
#             sum1 = sum1 + matrix[i][j]
#             sum2 = sum2 + matrix[j][i]
#         sum_row.append(sum1)
#         sum_coloumn.append(sum2)
#     sum3 = sum4 = 0
#     for i in range(len(matrix)):
#         sum3 = sum3 + matrix[i][i]
#         sum4 = sum4 + matrix[i][-i - 1]
#     if sum_row == sum_coloumn and sum3 == sum4:
#         for i in sum_row:
#             if i != sum3:
#                 return "not a magic matrix"
#         return f"it is a magic square matrix with magic sum {sum3}"
#     else:
#         return "not a magic matrix"
# print(fun([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))


# matrix=[[2,7,6],[9,5,1],[4,3,8]]
# sum_row=[]
# sum_coloumn=[]
# for i in range(len(matrix)):
#     sum1=sum2=0
#     for j in range(len(matrix[0])):
#         sum1=sum1+matrix[i][j]
#         sum2=sum2+matrix[j][i]
#     sum_row.append(sum1)
#     sum_coloumn.append(sum2)
# sum3=sum4=0
# for i in range(len(matrix)):
#     sum3=sum3+matrix[i][i]
#     sum4=sum4+matrix[i][-i-1]
# count=0
# if sum_row==sum_coloumn and sum3==sum4:
#     for i in sum_row:
#         if i==sum3:
#             count=count+1
#     if count==len(sum_row):
#         print(f"it is a magic square matrix with magic sum {sum3}")
#     else:
#         print("not a magic matrix")
# else:
#     print("not a magic matrix")


# def prime(num):
#     l=[int(i) for i in num.split(',')]
#     l.sort()
#     min=0
#     for i in l:
#         min=min*10+i
#     max=0
#     for i in l[::-1]:
#         max=max*10+i
#     difference = max-min
#     print(difference)
#     count=0
#     for i in range(1,difference+1):
#         if difference%i==0:
#             count=count+1
#     if count==2:
#         return "PRIME"
#     else:
#         return "NOT PRIME"
# num=input("Enter the commma separeted 4 digits :")
# print(prime(num))


# dic={'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}
# d={}
# l=[]
# for i in dic:
#     pass
# for k in range(len(dic[i])):
#     for i in dic:
#         v=dic[i]
#         d[i]=v[k]
#     l.append(d.copy())
# print(l)


# l=['bbb','c','aaaaaaaaaaa','dd']
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if len(l[i])>len(l[j]):
#             l[i],l[j]=l[j],l[i]
# print(l)


# m = [[1,2,3],[4,3,2],[2,6,3]]
# for i in m[0]:
#     c=0
#     for j in range(len(m)):
#         if i in m[j]:
#             c+=1
#     if c==len(m):
#         print(i)


# d={'a':1,'b':2,'c':3,'d':4,'e':5}
# v=[i for i in d.values()]
# p=input("Enter the key to pop :")
# d.pop(p)
# k=[i for i in d]
# v.pop()
# print(dict(zip(k,v)))


# s="Hello    Phantom  Blaze"
# print(" ".join(s.split()))

# l=[{'a':1,'b':2},{'a':3,'b':4},{'a':5,'b':6}]
# v=[list(i.values()) for i in l]
# k=[i for i in l[0]]
# v1=[[i[j] for i in v] for j in range(len(v[0]))]
# print(dict(zip(k,v1)))


from six.moves import configparser
parser = configparser.ConfigParser()
print(parser)