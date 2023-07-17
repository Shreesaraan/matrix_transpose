def transpose(r,c,matrix):
    temp=0
    for i in range(r):
        for j in range(c):
            if(i<j):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
    return matrix


matrix=[]
r=int(input("Number of Rows : "))
c=int(input("Number of Columns : "))
for i in range(r):
    matrix.append(list(map(int,input().split())))
print(transpose(r,c,matrix))
