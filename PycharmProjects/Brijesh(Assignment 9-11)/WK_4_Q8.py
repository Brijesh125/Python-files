from functools import reduce
def average(my_list):
    print("Average of positive numbers = ",end="")
    return (reduce(lambda a,b:a+b,[i for i in my_list if i>0]))/len([i for i in my_list if i>0])
my_list=[-1,2,-3,4,-5,1,-2,3,-4,5]
print(average(my_list))