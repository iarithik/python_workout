class flexibledict(dict):
   
    
    def __getitem__(self, key):
        try :
            if key in self:
                pass
            if str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
    
        return dict.__getitem__(self, key)


fd = flexibledict()
fd['a'] = 100
print(fd['a']) 
fd[5] = 500
print(fd[5]) 
fd[1] = 100 
print(fd['1']) 
fd['1'] = 100 
print(fd[1]) 