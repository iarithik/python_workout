def get_rainfall():
    city_dict ={}

    check = input("If you are ready to share information press any alphabet :")
    if bool(check) == False:
        print("See you later !")
    while bool(check): 
        city_ip = input("Please enter a city name : ")
        if city_ip == '':
            if bool(city_dict) == 0:
                print("No data available ")
            else:
                for key, value in city_dict.items():
                    print(f"{key}: {value}")
            break
        else:
            rainfall_ip = int(input("Please enter rainfall for the city"))
            if city_ip in city_dict:
                city_dict[city_ip] = city_dict.get(city_ip) + rainfall_ip
            else:
                city_dict.update({city_ip : rainfall_ip})
            
get_rainfall()