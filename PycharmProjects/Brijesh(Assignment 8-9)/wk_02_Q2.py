string=input("Enter the string : ")
ascii={}
list_ascii=[]
for i in range(256):
    ascii[i]=chr(i)
print("dict of ascii : ",ascii)
for s in string:
    for i,j in ascii.items():
        if s==j:
            list_ascii.append(i)
print("ascii of string : ",list_ascii)