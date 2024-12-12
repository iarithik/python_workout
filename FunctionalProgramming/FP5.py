def flip_dict(ip_dict):
    op = { value:key
          for key,value in ip_dict.items() }
    return op
    
print(flip_dict({'a':'1','b':'3'}))