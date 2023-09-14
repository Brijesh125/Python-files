file_name=input("Enter the file name : ") #matrix1.csv
                                          #matrix2.csv
                                          #matrix3.csv
f=open(file_name,'r')
matrix=[]
transpose=[]
for i in f:
    row=i.strip().split(",")
    for j in range(len(row)):
        if row[j].isnumeric():
            row[j]=int(row[j])
    matrix.append(row)
print("matrix : ",matrix)
for i in range(len(matrix[0])):
    matrix2 = []
    for j in range(len(matrix)):
        matrix2.append(matrix[j][i])
    transpose.append(matrix2)
print("transpose : ",transpose)
f.close()