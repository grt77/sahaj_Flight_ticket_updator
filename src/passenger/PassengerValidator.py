import os
from ..ConfigEnv import load_env_variables
import re
from datetime import datetime

'''
PassengerValidator.validator()->
helpful for validating the different kind of validations ,and getting which were errored out 

PassengerValidator.is_email_valid()->
helpful for validating the email using reg expression 

PassengerValidator.is_phone_number_valid()->
helpful for validating the phone number using reg expression 

PassengerValidator.is_fare_class_valid() and is_pnr_valid()->
same as above functions 

 
PassengerValidator.is_ticket_date_before_travel_date()->
helpful for finding whether travel date before the ticketdate or not 

PassengerValidator.is_booked_cabin_valid()->
helpful for checking booked cabin is valid or not 



'''


class PassengerValidator:
    def __init__(self):
        self.env_variables=load_env_variables()

    def validator(self,passenger):
        error_columns=''
        if not self.is_email_valid(passenger.Email):
            error_columns=error_columns+'Email,'
        if not self.is_phone_number_valid(passenger.Mobile_phone):
            error_columns=error_columns+'MOBILE_NUMBER,'
        if not self.is_fare_class_valid(passenger.Fare_class):
            error_columns=error_columns+'FARE_CLASS,'
        if not self.is_pnr_valid(passenger.Pnr):
            error_columns=error_columns+'PNR,'
        if not self.is_booked_cabin_valid(passenger.Booked_cabin):
            error_columns=error_columns+'BOOKED_CABIN,'
        if not self.is_ticket_date_before_travel_date(passenger.Ticketing_date,passenger.Travel_date):
            error_columns=error_columns+'TravelDate,'
        if error_columns=='':
            return None
        return error_columns[0:-1]


    def is_email_valid(self,email):
        return self.regex_checker(self.env_variables['EMAIL_REGEX'],email)

    def is_phone_number_valid(self,phone_number):
        return self.regex_checker(self.env_variables['MOBILE_NUMBER_REGEX'],phone_number)

    def is_fare_class_valid(self,fare_class):
        return self.regex_checker(self.env_variables['FARE_CLASS_REGEX'],fare_class)

    def is_pnr_valid(self,pnr):
        return self.regex_checker(self.env_variables['PNR_REGEX'],pnr)

    def is_ticket_date_before_travel_date(self,ticket_date,travel_date):
        try:
            ticket_date=datetime.strptime(ticket_date,str(self.env_variables['TICKET_DATE_FORMAT']))
            travel_date=datetime.strptime(travel_date,str(self.env_variables['TRAVEL_DATE_FORMAT']))
            print(ticket_date,travel_date)
            return ticket_date<travel_date
        except ValueError:
            return False

    def is_booked_cabin_valid(self,book_cabin):
        return  book_cabin in self.env_variables['TYPES_BOOKED_CABINS'].split(",")

    def regex_checker(self,re_expression,value):
        if re.match(re_expression,str(value)):
            return True
        else:
            return False


