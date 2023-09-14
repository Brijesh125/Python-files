def KeyValueExists(Dict,**key_value):
    count=0
    for i in key_value.items():
        if i in Dict.items():
            count+=1
        if count==len(key_value):
            return True
    else:
        return False

Dict={'a':'1','b':'2','c':'3','z':'26'}
print(KeyValueExists(Dict,a='1',b='2',z='26'))