# 20131113 Lab 21:30

# Expression statements
print "This module contains SPAM-related functions."

# Assert statements
assert age >= 12, "Children under the age 12 are not allowed!"

# Assignment Statements
x = 42  # Simple assignment
name, age = 'Gumby', 60  # Sequence unpacking
x = y = z = 10  # Chained assignments

# Augmented assignment statements
x *= 2  # Double x
x += 5  # adds 5 to x

# The pass statement
try x.name
except: AttributeError:
    pass
else:
    print "Hello", x.name

del x  # ubinds a variable
del seq[42]  # delete a sequence item
del seq[42:]  # delete a sequence slice  
del map['foo']  # delete a mapping item

# The print statement
print 'Hello, World!'
print 1, 2, 3
print >> somefile, 'xyz'
print 42,  # Writes '42' to sys.stdout



### Something terrible happened when I took practice with this git
### mode... And it turned out that I will omit some stuff...

# COmpound statement

# the if statement
# always remember to backup. Or you shall lose your face!!!
if x < 10:
    print 'Less than ten'
elif 10 <= x < 20:
    print 'Less than twenty'
else:
    print 'twenty or more'

# The while statement
x = 1
while x < 200:
    x *= 2  
print x

# The for statement
# The for statement is used for repeated execution over the elements
# of sequences or other iterable objects.
for i in range(10, 0, -1):
    print i
print 'Ignition!'

# The try statement
# The try statement is used to enclose pieces of code where one or
# more known exceptions may occur.
try:
    1/0
except ZeroDivisionError:
    print "Can't divide anything by zero."
finally:
    print "DOne trying to calculate 1/0"

# The with statement
# The with statement is used to wrap a block of code using a so-called
# context manager, allowing the context manager to perform some setup
# and cleanup actions.
with open("somefile.txt") as myfile:
    dosomething(myfile)
# The file will have been closed here

# Class definitions
# VIP. Class definitions are used to creat
