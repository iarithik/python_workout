menu ={ 'dosa':20,'idli': 25,'fries':40 , 'nuggets':80,'juice':20,'tea':10,'coffee':30}

def restaurant():
    total_count = 0
    check_order = input("Are you ready to order ? if YES press Y else N     :")
    total_order =" "

    while check_order == 'Y':
            cust_order = input("Please give your order")

            if cust_order in menu:
                total_count += menu.get(cust_order,0)
                total_order += cust_order 
            else:
                print("Please enter valid details")
            
            check_order = input("do you want to order  more ? if YES press Y else N    :")
            if check_order == 'N':
                break
    print(f" Your final order is  {total_order} and your bill is {total_count}")

if __name__ == "__main__":
    restaurant()



