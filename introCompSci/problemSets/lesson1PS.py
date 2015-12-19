#Python Programming 1

#Write Python code that prints out the number of hours in 7 weeks
day = 24 #hours
week = 7 #days
totalWeeks = 7

print totalWeeks * week * day

# Write Python code that stores the distance
# in meters that light travels in one
# nanosecond in the variable, nanodistance.

# These variables are defined for you:

speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion

# After your code, running the following:

# print nanodistance

# should output: 0.2998

# Note that nanodistance must be a decimal number.

# ASSIGN nanodistance BELOW this line

nanodistance = speed_of_light / nano_per_sec
print nanodistance

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print s[0:2] + t[3:]
#or
print s[:-2] + t[-3:]

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo"

# ENTER CODE BELOW HERE

print text.find("hoo")

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"

# ENTER CODE BELOW HERE

first_entry = text.find("zip")
second_entry = text.find("zip", first_entry + 1)
print second_entry

# Given a variable, x, that stores the
# value of any decimal number, write Python
# code that prints out the nearest whole
# number to x.
# If x is exactly half way between two
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved
# using just the information introduced in unit 1.

# x = 3.14159
# >>> 3 (not 3.0)
# x = 27.63
# >>> 28 (not 28.0)
# x = 3.5
# >>> 4 (not 4.0)

x = 3.14159
rounding = x + 0.5
new_string = str(rounding)
final_round = new_string.find('.')
answer = new_string[:final_round]
print answer



#ENTER CODE BELOW HERE
