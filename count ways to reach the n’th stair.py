'''
    There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either
    1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.
'''


def solution(num_stairs):
    counter = 0
    total = 0
    
    counter = count(num_stairs, counter, total+1)
    counter = count(num_stairs, counter, total+2)
    
    return counter


def count(num_stairs, counter, total):
    if total == num_stairs:
        return counter + 1
    elif total > num_stairs:
        return counter
    else:
        counter = count(num_stairs, counter, total+1)
        counter = count(num_stairs, counter, total+2)
        return counter
    