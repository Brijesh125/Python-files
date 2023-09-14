string_1 = "Life of Pie"
vowels=set("aeiouAEIOU")
c=0
for i in vowels:
    for j in string_1:
        if i==j:
            c=c+1
print("No of vowels :",c)