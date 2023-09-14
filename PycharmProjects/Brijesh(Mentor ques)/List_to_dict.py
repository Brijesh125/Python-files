#pseudocode
'''
step 1:assign 2 lists(keys and values)
step 2:create an empty dictionary as ans
step 3:concatenate keys and values into dict_list
step 4:use for loop in range of length of dict_list
       if i less than length of keys,key of ans is dict_list[i] and its value is dict_list[i+len(keys)
step 5:update the ans
step 6:print ans
'''

keys=["Ten","Twenty","Thirty"]
values=[10,20,30]
ans={}
dict_list=keys+values
for i in range(len(dict_list)):
    if i < len(keys):
        ans[dict_list[i]]=dict_list[i+len(keys)]
ans.update({"Fourty":40,"Fifty":50})
print("Dictionary :",ans)