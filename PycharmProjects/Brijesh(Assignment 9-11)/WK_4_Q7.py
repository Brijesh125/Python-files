from functools import reduce
def average(my_list):
    print("Average = ",end="")
    return (reduce(lambda a,b:a+b,my_list))/len(my_list)
my_list=[1,2,3,4,5,6,7,8,9,10]
print(average(my_list))