import numpy as np
str1='GXTXAYB'
str2='AGGTAB'
def LCS_Algo(A,B,mat):
    mat=[[0 for i in range(0,len(B)+1)]for j in range(0,len(A)+1)]
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i]==B[j]:
                mat[i+1][j+1]=1+mat[i][j]
            else:
                mat[i+1][j+1]=max(mat[i][j+1],mat[i+1][j])
    mat=np.array(mat)
    (u,v)=mat.shape
    (i,j)=(u-1,v-1)
    res=''
    while i>0 and j>0:
        if mat[i][j]>mat[i][j-1]:
            res=res+B[j-1]
            i=i-1
            j=j-1
        elif mat[i][j]==mat[i][j-1]:
            j=j-1
        else:
            i=i-1
    return res[::-1]
    
LCS_Algo(str1,str2,LCS(str1,str2))
