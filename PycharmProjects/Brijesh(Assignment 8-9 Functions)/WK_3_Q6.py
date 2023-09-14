def combinestrings(separator,*string):
    s=""
    for i in range(len(string)):
        if i==0:
            s=s+string[i]
        else:
            s=s+separator+string[i]
    return '"'+s+'"'

separator=input("Enter the separator string : ")
print(combinestrings(separator,"RED","BLUE","GREEN","ORANGE","YELLOW"))