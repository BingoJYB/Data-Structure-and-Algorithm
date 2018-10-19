import math


def solution(ls):
    sorted_ls = sorted(ls)
    max_dis = -math.inf
    for i in range(len(sorted_ls) - 1):
        if sorted_ls[i][1] >= sorted_ls[i + 1][0]:
            sorted_ls[i + 1][0] = sorted_ls[i][0]
        else:
            dis = sorted_ls[i][1] - sorted_ls[i][0]
            if dis > max_dis:
                max_dis = dis
    print(max_dis)
