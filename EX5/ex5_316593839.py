''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    if len(s) < 1:
        return s
    return s[-1:] + reverse_string(s[:-1])


#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    if len(lst) == 0:
        return -1
    elif len(lst) == 1:
        return lst[0]
    else:
        maxi = find_maximum(lst[1:])
    return maxi if maxi > lst[0] else lst[0]


#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    return len(s) < 2 or s[0] == s[-1] and is_palindrome(s[1:-1])


#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    if n == 1 or n == 0:
        return 1
    return climb_combinations(n-1) + climb_combinations(n-2)


#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    if len(s) == 0 and cnt == 0:
        return True
    elif len(s) == 0 and cnt < 0:
        return False
    if s.count('(') > s.count(')'):
        return False
    if s[0] == '(':
        return is_valid_paren(s[1:], cnt + 1)
    elif s[0] == ')':
        return is_valid_paren(s[1:], cnt - 1)
    else:
        return is_valid_paren(s[1:], cnt + 0)

#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
print(is_valid_paren("(.(a)") == False)
print(is_valid_paren("p(()r((0)))") == True)
print(reverse_string("abc") == 'cba')
print(reverse_string("Hello!") == '!olleH')

print(find_maximum([9,3,0,10]) == 10)
print(find_maximum([9,3,0]) == 9)
print(find_maximum([]) == -1)

print(is_palindrome("aa") == True)
print(is_palindrome("aa ") == False)
print(is_palindrome("caca") == False)
print(is_palindrome("abcbbcba") == True)

print(climb_combinations(3) == 3)
print(climb_combinations(10) == 89)



# ============================== END OF FILE =================================
