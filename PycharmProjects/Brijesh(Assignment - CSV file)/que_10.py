lis=[]
dic={}
file_name=input("Enter the file name : ") #role.csv
file=open(file_name,'r')
for i in file:
    row=i.strip().split(",")
    if '' in row:
        for j in range(row.count('')):
            row.remove('')
    lis.append(row)
for i in lis:
    dic[i.pop(0)]=i
print("Dictionary of data : ",dic)
name=input("Enter the name:")
if name not in dic:
    print("invalid user name")
else:
    role = input("Enter the role:")
    if role in dic[name]:
        print("True")
    else:
        print("False")
file.close()