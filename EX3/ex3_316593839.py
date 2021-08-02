''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_divisible_by_k(lst, k):
    count = 0
    for i in lst:
        if i % k == 0:
            count += i
    if count != 0:
        return count
    else:
        return 0


#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    count = 1
    lst = list(str(n))
    for i in lst:
        if int(i) % 2 != 0:
            count *= int(i)
    if count != 1:
        return count
    else:
        return 1


#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    longseq = ''
    for i in range(1, len(s)+1):
        if i * c in s:
            longseq = i *c
    return len(longseq)


#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    if type(lst) != list:
        return -1
    else:
        lst2 = []
        for x in lst:
            if type(x) != str:
                lst2.append(x)
            elif type(x) == str:
                lst2.append(x.upper())
        return lst2


#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):
    import copy
    newmat = copy.deepcopy(mat)
    for item, value in enumerate(newmat):
        for item2, value2 in enumerate(value):
            newmat[item][item2] = value2 // alpha
    return newmat


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    ver = []
    for x in range(len(mat[0])):
        ver.append([])
        for y in range(len(mat)):
            ver[x].append(mat[y][x])
    return ver

print(mat_transpose([[1,2], [3,4], [5,6]]))