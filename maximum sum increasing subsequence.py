'''
    Maximum Sum Increasing Subsequence
    Given an array of n positive integers. Write a program to find the sum of maximum sum
    subsequence of the given array such that the intgers in the subsequence are sorted in
    increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should
    be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output should be 22
    (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10
'''


def max_sum(arr):
    table = [0] * (len(arr))
    table[0] = arr[0]
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and table[i] < table[j] + arr[i]:
                table[i] = table[j] + arr[i]
            
    return max(table)
            

arr = [10, 5, 4, 3]
print(max_sum(arr))
    