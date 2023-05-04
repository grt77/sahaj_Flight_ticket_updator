from datetime import datetime

'''

This is used to get the datetime object providing format string 

'''

class DateOperations:
    def __init__(self,format_string):
        self.format_string=format_string
    def get_date_time_string(self):
        date_time_string=datetime.today().strftime(self.format_string)
        return date_time_string



