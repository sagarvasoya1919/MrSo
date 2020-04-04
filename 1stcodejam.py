import numpy as np

t=int(input())
for a in range(t):
    m=[]
    row=0
    column=0
    dia=0
    n=int(input())
    for w in range(n):
        item=list(map(int,input().split()))
        m.append(item)
    matrix=np.array(m)
    for i in range(len(matrix)):
        setr=set(matrix[i])
        if(len(setr)!=len(matrix[i])):
            row=row+1
        else:
            continue
    dia=np.trace(matrix)
    matrix2=matrix.transpose()
    for j in range(len(matrix2)):
        setc=set(matrix2[j])
        if(len(setc)!=len(matrix2[j])):
            column=column+1
        else:
            continue
    print("Case #{}: {} {} {}".format(a+1,dia,row,column))
