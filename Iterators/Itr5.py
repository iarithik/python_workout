def mychain(*args,**kwargs):
    for i in args:
        for j in i:
            yield j
    
    for i in kwargs:
        yield i

o = mychain('abc',[1,2,3],{'a':1, 'b':2}, c=3)
for i in o:
    print(i)