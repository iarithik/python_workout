num_list =[12,-5,9,-10,-50]


def positive_val(number):
	if number >=0:
		return number
	else:
		return number*(-1)

def check_value(num_list):
	top_val = max(num_list,key= positive_val)
	return top_val

print(check_value(num_list))
	
