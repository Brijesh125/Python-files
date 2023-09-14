def combinestrings(*string):
    s=""
    for i in range(len(string)):
        if i==0:
            s=s+string[i]
        else:
            s=s+","+string[i]
    return '"'+s+'"'

print(combinestrings("RED","BLUE","GREEN","ORANGE","YELLOW"))