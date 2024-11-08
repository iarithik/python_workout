city_dict ={}

def get_rainfall():

    check = input("If you are ready to share information press 'y' : ")
    if not check:
        print("See you later !")
    while check: 
        city_ip = input("Please enter a city name : ")
        if not city_ip:
            fetch_rainfall()
            break
        else:
            rainfall_ip = int(input("Please enter rainfall for the city  :"))
            set_rainfall(city_ip,rainfall_ip)
            
def set_rainfall(city,rainfall):
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

get_rainfall()