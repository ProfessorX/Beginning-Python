# Nested loop procedural style for finding big products
xs = (1,2,3,4)
ys = (10,15,3,22)
bigmuls = []
# ...more stuff...
for x in xs:
    for y in ys:
        # ...more stuff...
        if x*y > 25:
            bigmuls.append((x,y))
            # ...more stuff...
# ...more stuff...
print bigmuls


bigmuls = lambda xs,ys: filter(lambda (x,y):x*y > 25, combine(xs,ys))
combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
print bigmuls((1,2,3,4),(10,15,3,22))
