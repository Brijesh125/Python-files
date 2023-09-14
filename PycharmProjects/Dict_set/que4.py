dic = {2:"Apple",1:"Mango",3:"Orange",4:"Banana"}
keys=list(dic.keys())
keys.sort()
dict={}
for i in keys:
    for x,y in dic.items():
        if i==x:
            dict[i]=y
print(dict)