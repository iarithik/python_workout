d ={ 'a':1,'b':2,'d':'k'}
x = d.get('k')
print(x)

for key, value in d.items():
    print(f'{key}  {value}')

for key, value in enumerate(d):
    print(f'{key}  {value}')

s = {1,2,3} 
print(s)

so = [1,2,3,4,3,4,1]
xo = set(so)
print(xo)

s.add('a')
print(s)
s.update([10, 20, 30, 40, 50])
print(s)

