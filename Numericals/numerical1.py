import random
def guess_me( ):
    number = random.randint(10, 30)
    print("Guess a number between 1 to 100 inclusive")
    answer = True
    counter = 0

    while(answer):
        user_num = int(input("Enter your number here : "))
        if user_num == number:
            print(f'Ding ding you guessed the correct number!   the number is {number}' )
            answer = False
        elif user_num > number:
            print("Please choose a lower number")
        else:
            print("Please choose a higher number")
        counter +=1
        if counter == 3:
            print("Too bad ! Better luck next time!")
            break
if __name__ == "__main__":
    guess_me()