def run():
    stop_input = False
    counter = 0
    total = 0
    while not stop_input:
        user_rep = input("enter valid aaage")
        if user_rep =="":
            stop_input = True
            continue
        counter +=1
        print(f' Your daily runtime entered is {user_rep}')
        total += int(user_rep)
    if counter < 1:
        print("Please enter valid details")
    else:
        avg = float(total/counter)
        print(f'Your avg runtime is {avg}')

run()