def binary_search(my_list,target):
    start = 0
    stop = len(my_list) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if target == my_list[mid]:
            print("index of target : ", end="")
            return mid
        elif target < my_list[mid]:
            stop = mid - 1
        else:
            start = mid + 1

    if stop < 0:
        print("index of closest number : ",end="")
        return 0
    elif start >= len(my_list):
        print("index of closest number : ", end="")
        return len(my_list) - 1
    elif abs(target - my_list[start]) < abs(target - my_list[stop]):
        print("index of closest number : ", end="")
        return start
    else:
        print("index of closest number : ", end="")
        return stop

n = int(input("Enter number of elements : "))
my_list = []
for i in range(n):
    elements = int(input(f"Enter the index {i} element : "))
    my_list.append(elements)
my_list.sort()
print(my_list)
target = int(input("Enter the target : "))

print(binary_search(my_list,target))