"""makes=["Honda","Toyota","Ford","Nissan","Hyundai"]
models=["Honda Civic","Honda Accord","Toyota Corolla","Toyota Camry","Ford Fusion","Ford Escape","Nissan Sentra","Hyundai Elantra"]

def makes_model(makes,models):
    models_list=[[i for i in models if x in i] for x in makes]
    dic=dict(zip(makes,models_list))
    return dic
print(makes_model(makes,models))

def model1(makes,models):
    models=list(map(lambda x:[x[len(i)+1:] for i in makes if i in x],[x for x in models]))
    models = [i[0] for i in models]
    return models
print(model1(makes,models))

def model2(makes,models):
    models = [[x[len(i)+1:] for i in makes if i in x] for x in models]
    models=[i[0] for  i in  models]
    return models
print(model2(makes,models))

from functools import reduce
def string_models(makes,models):
    models = [[x[len(i)+1:] for i in makes if i in x] for x in models]
    models=[i[0] for  i in  models]
    string = reduce(lambda a,b:a+","+b,models)
    return '"'+string+'"'
print(string_models(makes,models))"""