def flatten(*list_of_list):
    x = [ j
            for i in list_of_list for j in i]
    print(x)

flatten([1,2],[3,4])