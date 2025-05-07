import ast
step = ast.literal_eval(input())
current = 0
sumBrick = 0
for s in step :
    if(s > current) :
        sumBrick += (s-current)
    current = s
print(sumBrick)