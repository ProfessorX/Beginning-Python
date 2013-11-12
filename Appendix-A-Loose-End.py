# 20131113 Lab 02:00
import math
x = math.sqrt(y)

# or something like this
from math import sqrt
x = sqrt(y)

# You want to add something like this at the end of your program
if __name__ == "__main__": main()

# On UNIX, use the following line to make it run by itself
#!/usr/bin/env python

# You can aviod some problems by try/except statement
def safe_division(a, b):
    try:
        return a/b
    except:
        ZeroDivisionError

# More dummy changes 




