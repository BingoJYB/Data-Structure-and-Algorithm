'''
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of
    a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
    permutation is a rearrangement of letters. The palindrome does not need to be limited to just
    dictionary words.
    EXAMPLE
    Input: Tact Coa
    Output: True (permutations: "taco cat'; "atc o eta·; etc.)
'''

def solution(string):
    string = string.lower()
    string = ''.join(string.split(' '))
    dic = {}
    count_odd = 0
    
    for c in string:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
            
        if dic[c] % 2:
            count_odd += 1
        else:
            count_odd -= 1
    
    if count_odd == 1 or count_odd == 0:
        return True
    else:
        return False
    
