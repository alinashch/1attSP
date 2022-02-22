

def sol1(list1):
    print(list1)
    solution1(list1)
    print(list1)
    print()

def solution1(list):
    for i in list:
        n=list.count(i)
        if(n>1):
         while(n>0):
            list.remove(i)
            n=list.count(i)
    return list

if __name__ == '__main__':
    list1 =[1,0, 3,5,1,7,4,6,4,3,8,9,0,2,1]
    list2=[2,2,2,2,2,2,2,2,2]
    list3=[-1,1,-1,4,3,2,-6,7,-8,1]
    list4=[0,1,2,3,4,5,6,7,8,9,10]
    list5=[0,0,0,0,0,0,1]
    sol1(list1)
    sol1(list2)
    sol1(list3)
    sol1(list4)
    sol1(list5)

def solution2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()
    sol2(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()
    print()

def sol2(matrix):
    MaxN=0
    N=0
    a = []
    b = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            a.append(matrix[j][i])
        Max=max(a)
        a.clear()
        if Max>MaxN:
            N=i
            MaxN=Max
    MinN=MaxN
    K=0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            b.append(matrix[j][i])
        Min=min(b)
        b.clear()
        if Min<=MinN:
            K=i
            MinN=Min
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==N:
                a.append(matrix[j][i])
            if i==K:
                b.append(matrix[j][i])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==N:
                matrix[j][i]=b[j]
            if i==K:
                matrix[j][i]=a[j]
    return matrix

if __name__ == '__main__':
    matrix1=[[1,1,0],[0,0,0],[0,6,0]]
    solution2(matrix1)
    matrix2=[[10,0,0,10],[10,0,0,10],[10,0,0,10],[10,0,0,10] ]
    solution2(matrix2)
    matrix3=[[-2,-5,0,9], [2,5,1, -5],  [7,9,2,6],[1,7,-2,3]]
    solution2(matrix3)
    matrix4=[[2,-10,0, 7], [1, 10, 2,3], [8,9,-1,2], [3,5,6,7]]
    solution2(matrix4)

def solution3(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()
    print()

    a = sol3(matrix)
    print(a)

def sol3(matrix):
    a=[]
    for i in range(len(matrix)):
        print(matrix[i][2])
        x=matrix[i][0]
        y=matrix[i][1]
        max=matrix[i][2]
        for j in range(i+1, len(matrix)):
            if matrix[j][0]==x & matrix[j][1]==y:
                if(matrix[j][2]>=max):
                    max=matrix[j][2]
                a.clear()
                a.append(x)
                a.append(y)
                a.append(max)
    return a


if __name__ == '__main__':
    matrix1=[[1,1,0], [1,1,3],[1,1,2], [2,3,4], [2,3,5], [2,3,8]]
    solution3(matrix1)