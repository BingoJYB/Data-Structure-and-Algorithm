'''
	Given a string, your task is to reverse only the vowels of string.

	Examples:
	
		Input: hello
		Output: holle

		Input: hello world
		Output: hollo werld
'''

def swap(str_ls, x, y):
    temp = str_ls[x]
    str_ls[x] = str_ls[y]
    str_ls[y] = temp

    return str_ls


def solution(string):
    s = list(string)
    vowel = 'aeiouAEIOU'
    head = 0
    tail = len(s) - 1

    while head <= tail:
        if s[head] not in vowel:
            head = head + 1

        if s[tail] not in vowel:
            tail = tail - 1
            
        if s[head] in vowel and s[tail] in vowel:
            swap(s, head, tail)
            head = head + 1
            tail = tail - 1

    print(''.join(s))
