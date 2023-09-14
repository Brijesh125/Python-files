#1
"""
def fun(list1,num):
    power=[i**num for i in list1]
    return power
print(fun([1,2,3],2))
"""
#2
makes=["Honda","Toyota","Ford","Nissan","Hyundai"]
models=["Honda Civic","Honda Accord","Toyota Corolla","Toyota Camry","Ford Fusion","Ford Escape","Nissan Sentra","Hyundai Elantra"]
"""
def makes_model(makes,models):
    models=[[i for i in models if x in i] for x in makes]
    dic={i:j for i,j in zip(makes,models)}
    return dic
print(makes_model(makes,models))
"""
"""
def makes_model(makes,models):
    models_list=[]
    for i in range(len(makes)):
        lis=[j for j in models if j.startswith(makes[i])]
        models_list.append(lis)
    dic={i:j for i,j in zip(makes,models_list)}
    return dic
print(makes_model(makes,models))
"""
#3
"""
def model1(models):
    return list(map(lambda x:x.split().pop(1),models))
print(model1(models))
"""
"""
def model1(makes,models):
    return list(map(lambda x:[x[len(i)+1:] for i in makes if i in x].pop(0),models))
print(model1(makes,models))
"""
#4
"""
def model2(models):
    return [x.split().pop(1) for x in models]
print(model2(models))
"""
"""
def model2(makes,models):
    return [x[len(i)+1:] for i in makes for x in models if i in x]
print(model2(makes,models))
"""
#5
"""
from functools import reduce
def string_models(models):
    models = [x.split().pop(1) for x in models]
    string = reduce(lambda a, b: a + "," + b, models)
    return '"'+string+'"'
print(string_models(models))
"""
"""
from functools import reduce
def string_models(makes,models):
    models = [x[len(i)+1:] for i in makes for x in models if i in x]
    string = reduce(lambda a,b:a+","+b,models)
    return '"'+string+'"'
print(string_models(makes,models))
"""
#6
"""
def C_to_F(C):
    x=lambda x:(x*9/5)+32
    return [x(i) for i in C]
C=[0,10,21,30,37,40,100,180]
print(C_to_F(C))
"""
#7
"""
from functools import reduce
def average(my_list):
    return (reduce(lambda a,b:a+b,my_list))/len(my_list)
my_list=[1,2,3,4,5,6,7,8,9,10]
print(average(my_list))
"""
#8
"""
from functools import reduce
def average(my_list):
    new_list=[i for i in my_list if i>0]
    return (reduce(lambda a,b:a+b,new_list))/len(new_list)
my_list=[-1,2,-3,4,-5,1,-2,3,-4,5]
print(average(my_list))
"""
#9
"""
def ascii(string):
    ascii={chr(i):i for i in range(256) if chr(i) in string}
    result={i:ascii[i] for i in string}
    print("result : ", result)
    print("List of ascii : ", end="")
    return [i for i in result.values()]
print(ascii("Brijesh"))
"""
#10
"""
def names(my_list):
    new_list=[i.split() for i in my_list]
    return {new_list[i][1]:new_list[i][0] for i in range(len(new_list))}
my_list=['Binu K.B','Brijesh K.Babu','Bindu Babu','Babu K.S']
print(names(my_list))
"""