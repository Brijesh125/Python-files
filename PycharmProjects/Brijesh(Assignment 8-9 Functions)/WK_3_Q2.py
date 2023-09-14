def ascii(string):
    ascii = {}
    list_ascii = []
    result={}
    for i in range(256):
        ascii[i] = chr(i)
    for s in string:
        for i, j in ascii.items():
            if s == j:
                result[s]=i
                list_ascii.append(i)
    print("List of ascii : ", list_ascii)
    print("result : ",end="")
    return result

string=input("Enter the string : ")
print(ascii(string))