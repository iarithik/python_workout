from decimal import Decimal

location_tax_dict ={ 'Chico': Decimal('0.5'),'Groucho': Decimal('0.7') ,'Harpo': Decimal('0.5'),'Zeppo': Decimal('0.4')}
def calculate_tax(cost,location,hour):
    location_tax = location_tax_dict.get(location.title())
    tax = cost*location_tax* Decimal((hour/24))

    return tax

calculate_tax(500,'chico',12)