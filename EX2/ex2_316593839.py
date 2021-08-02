""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 2  # Replace the assignment with a positive integer to test your code.
A = [1, 2, 3, 4, 5]  # Replace the assignment with other lists to test your code.


# Write the code for question 2 using a for loop below here.
count = 0
for index, value in enumerate(A):
    if value % a == 0:
        print(index)
        count += 1
        break
if count == 0:
    print('-1')

# Write the code for question 2 using a while loop below here.

# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
B = ['hello', 'world', 'course', 'python', 'day']
# Replace the assignment with other lists of strings (str) to test your code.
count = 0
max_count = 0
for item in B:
    for letter in item:
        count += 1
avr = count/len(B)
for item in B:
    if len(item) > avr:
        max_count += 1
print('The number of strings longer than the average is:', max_count)

# Write the rest of the code for question 2 below here.
counter = 0
max_counter = 0
i = 0

while i < len(B):
    counter += len(B[i])
    i +=1

i = 0
avr = counter/len(B)

while i < len(B):
    if len(B[i]) >avr:
        max_counter += 1
    i += 1
print('The number of strings longer than the average is:', max_counter)


# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

C = [0, 1, 2, 3, 4]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 3 below here.
i = 0
summ = 0
while i+1 < len(C):
    if len(C) == 0:
        break
    else:
        summ += C[i]*C[i+1]
        i += 1
if len(C) == 1:
    summ += C[0]

print(summ)


# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

#D = [1, 2, 4, 7]  # Replace the assignment with other lists to test your code.
D = [1, 2, 4, 8, 10, 13, 18]
# Write the rest of the code for question 4 below here.
i = 0
sum = [D[0] - D[1]]
new = []
new.append(D[0])
new.append(D[1])
while i < len(D)-2:
    sum_2 = D[i+1] - D[i+2]
    if abs(sum_2) > abs(max(sum)):
        new.append(D[i+2])
        sum.append(abs(sum_2))
    i += 1
print(new)


# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaaadddefggg'  # Replace the assignment with other strings to test your code.
k = 2  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.
count = 0
for i in my_string:
    if i*k in my_string:
        print('For length {}, found the substring {}!'.format(k, i*k))
        count += 1
        break
if count == 0:
    print("Didn't find a substring of length {}".format(k))



# End of code for question 5