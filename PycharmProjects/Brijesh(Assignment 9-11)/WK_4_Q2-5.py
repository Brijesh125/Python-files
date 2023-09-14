makes=["Honda","Toyota","Ford","Nissan","Hyundai"]
models=["Honda Civic","Honda Accord","Toyota Corolla","Toyota Camry","Ford Fusion","Ford Escape","Nissan Sentra","Hyundai Elantra"]

#2
def makes_model(makes,models):
    print("2.Dictionary of makes and models : ",end="")
    return {i:j for i,j in zip(makes,[[i for i in models if x in i] for x in makes])}
print(makes_model(makes,models))

#3
def model1(models):
    print("3.List with map and lambda : ",end="")
    return list(map(lambda x:x.split().pop(1),models))
print(model1(models))

#4
def model2(models):
    print("4.List with list comprehension : ", end="")
    return [x.split().pop(1) for x in models]
print(model2(models))

#5
from functools import reduce
def string_models(models):
    print("5.comma separated string with reduce : ",end="")
    return '"'+reduce(lambda a, b: a + "," + b,[x.split().pop(1) for x in models])+'"'
print(string_models(models))