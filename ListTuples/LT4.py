import _collections_abc
import collections

def most_repeating_word(*str_ip):
    count_el =0
    op_string =""
    for element in str_ip:
        cur_val = count_str(element)
        if  cur_val> count_el:
            count_el = cur_val
            op_string = element
    print(f"The word with most repeated letters is {op_string}")
    

def count_str(string):
    str_dict ={}
    # count = 1
    # for i in string:
    #     if i in str_dict:
    #         str_dict[i] = str_dict.get(i)+1
    #     else:
    #         str_dict.update({i:count})

    str_dict = collections.Counter(string)
    max_count = max(str_dict.values())
    return max_count

if __name__ == "__main__":
    most_repeating_word('this', 'is', 'an', 'elementary', 'test', 'example','ggggg')
