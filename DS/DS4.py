def dictdiff(dict1, dict2):
    #approach 1
    dict_out = { }

    for key,value in dict2.items():
        if key not in dict1:
            dict_out.update({key:[dict1.get(key),value]})

    for key,value in dict1.items():
        if key in dict2:
            if value != dict2.get(key):
                dict_out.update({key :[value,dict2.get(key)]})
        elif key not in dict2:
            dict_out.update({key:[value,dict2.get(key)]})
    sorted_dict = dict(sorted(dict_out.items()))

    return sorted_dict

    #approach 2
    # output = {}

    # dict_out = dict1.keys() | dict2.keys()
    # for key in dict_out:
    #     if dict1.get(key) != dict2.get(key):
    #         output[key]= [dict1.get(key),dict2.get(key)]
    # return output
  


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1, d1)) 
print(dictdiff(d1, d2)) 
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3, d4)) 
d5 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1, d5)) 
