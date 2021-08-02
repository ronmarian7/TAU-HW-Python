''' Exercise #1 - Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
R = 5.0 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.
pie = 3.14
Diameter = 2*R

Circumference = 2*pie*R
Area = pie*(R**2)
print('Diameter is:', Diameter)
print('Circumference is:', Circumference)
print('Area is:', Area)


#########################################
# Question 2 - do not delete this comment
#########################################
S = 'Hello, dear world!' # Replace ??? a string of your choice.
# Write the rest of the code for question 2 below here.
l = len(S)
if l >= 10:
    first = S[:10]
    after = S[10:]
    print(first.lower() + after.upper())
else:
    print('$' + S[1:-1] + '@')








#########################################
# Question 3 - do not delete this comment
#########################################
number = -6 # Replace ??? with a int of your choice.
# Write the rest of the code for question 3 below here.
if number % 2 == 0:
    print('I am {} and I am even'.format(number))
else:
    print('I am {} and I am odd'.format(number))




#########################################
# Question 4 - do not delete this comment
#########################################
a = 9 # Replace ??? with a positive int of your choice.
b = 5  # Replace ??? with a positive int of your choice.
c = 5  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.
one = (a+b)**(1/c)
two = (a**b)**(1/c)
three = (a/b) - (b/c)
print("{:.5f}".format(one))
print("{:.5f}".format(two))
print("{:.5f}".format(three))



#########################################
# Question 5 - do not delete this comment
#########################################
year = 2000 # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 5 below here.

if year % 4 == 0 and not year % 100 == 0:
    print('{} is a leap year'.format(year))
elif year % 400 == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))




