test_data_email_validation = [
    ('gattupalliravi1@gmail.com', True),
    ('radhika@zzz', False),
    ('kben@zzz.com', True),
    ('1234', False),
    (1234, False)
]

test_data_phone_number_validation = [
    (9848517421, True),
    (123456, False),
    (8919006032, True),
    (876534547, False)
]

test_data_fare_class_validation = [
    ('A',True),
    ('AB',False),
    ('a',False),
    ('Z',True),
    (12,False)
]



test_data_pnr_validation = [
    ('PQ234',False),
    ('QWE123',True),
    (123,False),
    ('ABCD23',True),
    ('ZZZ345',True),
    ('A1B2C3',True)
]



test_data_book_cabin_validation = [
    ('Economy',True),
    ('Premium Economy',True),
    ('Premium',False),
    ('First',True),
    ('Busines',False)
]


test_data_schema_columns_validation = [
    (["First_name","Last_name","PNR","Fare_class","Travel_date","Pax","Ticketing_date","Email","Mobile_phone","Booked_cabin"],True),
    (["First_name","Last_name","PNR","Fare_class","Travel_date","Pax","Ticketing_date","Email","Mobile_phone","Booked_cabin","Teja"],True),
    (["First_name","Last_name","PNR","Fare_class","Travel_date","Ticketing_date","Email","Mobile_phone","Booked_cabin"],False)
]