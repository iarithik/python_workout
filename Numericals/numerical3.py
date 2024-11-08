def avgrun():
    total = 0
    avg = 0
    counter = 0
    while True:
        user_rep = input("Enter your daily runtime :")
        if not user_rep:
            break    
        counter +=1
        print(f' Your daily runtime entered is {user_rep}')
        total += int(user_rep)
    if counter < 1:
        print("Please enter valid details")
    else:
        avg = float(total/counter)
        print(f'Your avg runtime is {avg}')

if __name__ == "__main__":
    avgrun()