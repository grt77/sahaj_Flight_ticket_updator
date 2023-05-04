'''

created a class for storing the object in memory , it will be used for later purpose

'''


class Passenger:
    def __init__(self,passenger_dict):
        self.First_name=passenger_dict['First_name']
        self.Last_name=passenger_dict['Last_name']
        self.Pnr=passenger_dict['PNR']
        self.Fare_class=passenger_dict['Fare_class']
        self.Travel_date=passenger_dict['Travel_date']
        self.pax=passenger_dict['Pax']
        self.Ticketing_date=passenger_dict['Ticketing_date']
        self.Email=passenger_dict['Email']
        self.Mobile_phone=passenger_dict['Mobile_phone']
        self.Booked_cabin=passenger_dict['Booked_cabin']

