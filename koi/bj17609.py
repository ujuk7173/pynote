# 회문


def is_palindrome(s):
    return s == s[::-1]

def is_almost_palindrome(s):
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]
        check_palindrome = is_palindrome(new_s)
        print(new_s, check_palindrome)

        if check_palindrome:
            return True

    return False
#driver code
t = int(input()) 
lst = []
for _ in range(t):
    s = input()
    lst.append(s)
for s in lst:
    res = is_palindrome(s)
    if res == True:
        print(0)
    else:
        res = is_almost_palindrome(s)
        if res == True:
            print(1)
        else:
            print(2)



# others
def check_for_palindrome(s):
    return s == s[::-1]
def is_almost_palindrome_v1a(s):
    """
    'True' if there is at least one option that is palindrome.
    """
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]
        is_palindrome = check_for_palindrome(new_s)
        print(new_s, is_palindrome)

        if is_palindrome:
            return True

    return False






