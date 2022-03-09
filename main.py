import dictionary as dictionary
import numpy as np
from collections import defaultdict


def sol1(list1):
    print(list1)
    v = solution1(list1)
    print(v)
    print()


def solution1(list):
    v = [x for x in list if list.count(x) == 1]
    return v


if __name__ == '__main__':
    list1 = [1, 0, 3, 5, 1, 7, 4, 6, 4, 3, 8, 9, 0, 2, 1]
    list2 = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    list3 = [-1, 1, -1, 4, 3, 2, -6, 7, -8, 1]
    list4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list5 = [0, 0, 0, 0, 0, 0, 1]
    sol1(list1)
    sol1(list2)
    sol1(list3)
    sol1(list4)
    sol1(list5)


def solution2(matrix):
    matrix=np.array(matrix)
    print(matrix)
    matrix=soll2(matrix)
    print()
    print(matrix)
    print()


def soll2(matrix):
    n = 0
    k = 0
    q = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == np.amin(matrix):
                k = j
            if matrix[i][j] == np.amax(matrix):
                if q == 0:
                    q = 10
                    n = j

    print(k, n)
    matrix=matrix.transpose()
    matrix[[k,n]] = matrix[[n,k]]
    matrix1=matrix.transpose()
    return matrix1


if __name__ == '__main__':
    matrix1 = [[1, 1, 0], [0, 0, 0], [0, 6, 0]]
    solution2(matrix1)
    matrix2 = [[10, 0, 0, 10], [10, 0, 0, 10], [10, 0, 0, 10], [10, 0, 0, 10]]
    solution2(matrix2)
    matrix3 = [[-2, -5, 0, 9], [2, 5, 1, -5], [7, 9, 2, 6], [1, 7, -2, 3]]
    solution2(matrix3)



def solution3(matrix):
    dict = defaultdict(list)
    for i in range(len(matrix)):
        x = matrix[i][0];
        y = matrix[i][1];
        if y == 0:
            k = x
        else:
            k = x / y
        a=[x,y,matrix[i][2]]
        dict[k].append(a)
    q=dict.keys()
    for i in q:
        print(max(dict[i]))


if __name__ == '__main__':
    matrix1 = [[2, 3, 4],[1, 1, 0], [1, 1, 3],   [2, 3, 5],[1, 1, 2], [2, 3, 8]]
    solution3(matrix1)





def solution4(string):
    if string.find("(") != -1:
        while string.find("(") != -1:
            x = string.find("(")
            y = string.find(")")
            z = string.find("(", x + 1)
            if z < y:
                while z > x & x < y:
                    x = z
                    z = string.find("(", x)
                string = string[0:int(x)] + string[int(y + 1):int(len(string))]
            else:
                string = string[0: x] + string[y + 1: len(string)]
    return string


if __name__ == '__main__':
    S1 = "Выбрать (в виде списка) из текста все даты"
    S1 = solution4(S1)
    print(S1)
    s2 = "Написать (функцию) представления числа (до миллиона включительно) в виде строки" + " Обработать текст (следующим образом: (в конце каждого слова))  "
    s2 = solution4(s2)
    print(s2)
    s3 = "Программа разработана на C# (С# (произносится си шарп) – объектно-ориентированный язык программирования) студентами ВГУ (Воронежский государственный университет)!"
    s3 = solution4(s3)
    print(s3)
    s4 = "(())стр(о)ка"
    s4 = solution4(s4)
    print(s4)
    s5 = "(в виде списка)"
    s5 = solution4(s5)
    print(s5)
