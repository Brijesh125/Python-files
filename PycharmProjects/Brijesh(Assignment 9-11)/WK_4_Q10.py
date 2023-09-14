def names(my_list):
    new_list=[i.split() for i in my_list]
    return {new_list[i][1]:new_list[i][0] for i in range(len(new_list))}
my_list=['Binu K.B','Brijesh K.Babu','Bindu Babu','Babu K.S']
print(names(my_list))