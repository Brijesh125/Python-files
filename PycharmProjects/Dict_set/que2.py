list_2=[1,"a",2,"b",3,"c"]
dic={}
for i in range(0,len(list_2)-1,2):
    dic[list_2[i]]=list_2[i+1]
print(dic)