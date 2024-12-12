
def transform_values( func, ip_dict):
    op = { key : func(value) for key,value in ip_dict.items() }
    return op

print(transform_values(lambda x: x*x ,{'a':10,'b':4,'c':5}))