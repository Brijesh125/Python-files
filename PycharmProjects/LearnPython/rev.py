# s="NSWE"
# l=[]
# l1=[]
#
# for a in s:
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     for f in s:
#                         for g in s:
#                             for h in s:
#                                 l.append(a+b+c+d+e+f+g+h)
#
# for i in l:
#     if i.count("N")>=2:
#         l1.append(i)
#
# for i in l1:
#     l2=list(i[:4])
#     l3=list(i[4:])
#     for j in range(len(l3)):
#         if l3[j]=="N":
#             l3[j]="S"
#         elif l3[j]=="S":
#             l3[j]="N"
#         elif l3[j]=="E":
#             l3[j]="W"
#         else:
#             l3[j]="E"
#     if l2==l3[::-1]:
#         print(i)

