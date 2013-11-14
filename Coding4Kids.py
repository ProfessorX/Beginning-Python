for i in range(10, 0, -1):
    print i

print 'Ignition!'

# Something more fun
try:
    1/0
except ZeroDivisionError:
    print "Can't divide anything by zero."
finally:
    print "DOne trying to calculate 1/0"

