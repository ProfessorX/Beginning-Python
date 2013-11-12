# 20131112 Lab 18:18
# Always remember the *self* argument

# 20131113 Lab 01:30
def __init__(self, contents=None):
    self.contents = contents or []

def add(self, element):
    self.contents.append(element)

def print_me(self):
    result = ""
    for element in self.contents:
        result = result + "" + repr(element)
    print "Contains:" + result

# Objects and stuff
if a:
    print a
else:
    print b

# We could rewrite like this
print a or b

# Basket constructor
if contents:
    self.contents = contents
else:
    self.contents = []

# A simple statement
self.contents = contents or []

# Use an empty list as default value
def __init__(self, contents=[]):
    self.contents = contents[:]

# Make a basket and to use it.
b = Basket(['apple','orange'])
b.add("lemon")
b.print_me()


