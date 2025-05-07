import ast

matrixstr = ""
while True :
    line = input().strip()
    matrixstr += line
    if(line[-1] == "]") :
        break
matrix = ast.literal_eval(matrixstr)
n = len(matrix)
ans = []
for j in range(0,len(matrix[0])) :
    if(j % 2 == 0) :
        for i in range(0,n) :
            ans.append(matrix[i][j])
    else :
        for i in range(n-1,-1,-1) :
            ans.append(matrix[i][j])
print(','.join(str(x) for x in ans))