city_dict ={}

def get_rainfall():

    check = input("If you are ready to share information press 'y' : ").strip()
    if not check:
        print("See you later !")
    else:
        set_rainfall(check)
            
def set_rainfall(check):
    while check: 
        city = input("Please enter a city name : ").strip().title()
        if not city:
            fetch_rainfall()
            break
        else:
            try:
                rainfall = int(input("Please enter rainfall for the city  :").strip())
            except ValueError:
                print("why are you dogshit, enter proper details or get lost!!")
                continue
        if city in city_dict:
            city_dict[city] = city_dict.get(city) + rainfall
        else:
            city_dict.update({city : rainfall})

def fetch_rainfall():
    if not city_dict :
        print("No data available ")
    else:
        for key, value in city_dict.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    get_rainfall()

#ctrl + []  for indentation