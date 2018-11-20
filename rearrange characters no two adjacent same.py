'''
    Rearrange characters in a string such that no two adjacent are same

    Given a string with repeated characters, task is rearrange characters
    in a string so that no two adjacent characters are same
'''


def rearrange_character(str):
    res = ''

    if len(str) == 0 or len(str) == 1:
        res += str
    else:
        res = rearrange_character_util(str, res, len(str))

    if len(res) == len(str):
        print(res)
    else:
        print('Not Possible')


def rearrange_character_util(str, res, total_len):
    if str == '':
        return res

    for i in range(len(str)):
        c = str[i]

        if len(res) > 0 and c == res[-1]:
            continue

        remaining = str[:i] + str[i + 1:]
        res = rearrange_character_util(remaining, res + c, total_len)

        if len(res) == total_len:
            break

    return res


rearrange_character('aaaabcc')
