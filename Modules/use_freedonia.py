from decimal import Decimal
from freedonia import calculate_tax, location_tax_dict

def tax_return():
    try:
        location = input("Please enter the location of purchase").strip().title()        
        if location not in location_tax_dict:
            raise ValueError(f'Be better, give valid details, I can only handle so much')
        cost = Decimal(input("Please enter the total cost of purchase").strip())
        hour = int(input("Please enter hour of purchase in 24 hour format or break me").strip())
        if hour not in range(1,25):
            raise ValueError("You don't listen do you, I have sent police to your place , enjoy tax evasion")

        tax = calculate_tax(cost,location,hour)

        total_cost = tax + cost

        return f'You need to pay up , amount : {total_cost}'
    except ValueError as e:
        print(f" Error {e}")
        return None
    except Exception as e:
        print(f" sike! bad luck better luck next time, {e}")
        return None

result = tax_return()
if result :
    print(result)