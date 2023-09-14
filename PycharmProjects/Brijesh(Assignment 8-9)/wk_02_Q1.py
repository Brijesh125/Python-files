#input

n=int(input("Enter number of elements : "))
my_list=[]
for i in range(n):
    elements=int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
print("list = ",my_list)
target=int(input("Enter the target : "))

#sorting

for i in range(n):
    for j in range(i+1,n):
        if my_list[i] > my_list[j]:
            my_list[i],my_list[j]=my_list[j],my_list[i]
print("sorted list = ",my_list)

#Binary search

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