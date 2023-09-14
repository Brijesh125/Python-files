file_name=input("Enter the file name : ") #dict1.csv
                                          #dict2.csv
                                          #dict3.csv
f=open(file_name,'r')
dic={}
for i in f:
    items=i.strip().split(",")
    for i in range(2):
        if items[i].isnumeric():
            items[i]=int(items[i])
    dic[items[0]]=items[1]
print("Dictionary : ",dic)
f.close()