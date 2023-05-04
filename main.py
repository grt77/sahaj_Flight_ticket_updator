from src.Date_time_oper.DateOperations import DateOperations
from src.ConfigEnv import load_env_variables
from src.Files_oper.FileOperations import FileOperations
from src.Files_oper.FileManager import FileManager
from src.passenger.Passenger import Passenger
from src.passenger.PassengerValidator import PassengerValidator
from src.discount_offer.DiscountCoupon import DiscountCoupon
from src.schema.SchemaValidation import SchemaValidation
import sys


def run_pipeline():
    env_var=load_env_variables()
    file_format_date_obj=DateOperations(env_var['FILE_DATE_FORMAT'])
    file_format_date=file_format_date_obj.get_date_time_string()
    file_format_time_obj=DateOperations(env_var['FILE_TIME_FORMAT'])
    file_format_time=file_format_time_obj.get_date_time_string()
    input_file_obj=FileOperations(filename='',date_of_file=file_format_date,time_of_file=file_format_time)
    input_file_path=input_file_obj.get_input_file_path()
    input_file_manager=FileManager(input_file_path)
    input_file_headers=input_file_manager.get_headers_file()
    schema_validation_object=SchemaValidation(set(input_file_headers))
    if not (schema_validation_object.is_schemaColumns_valid()):
        sys.exit("Schema is not valid, please check with file")
    passenger_validator_obj=PassengerValidator()
    output_succ_file_obj=FileOperations(kind_of_file='success',date_of_file=file_format_date,time_of_file=file_format_time,filename='passenger_details',type_of_folder='OUTPUT_FOLDER')
    output_error_file_obj=FileOperations(kind_of_file='error',date_of_file=file_format_date,time_of_file=file_format_time,filename='passenger_details',type_of_folder='OUTPUT_FOLDER')
    output_succ_file_path=output_succ_file_obj.generate_file_path()
    output_error_file_path=output_error_file_obj.generate_file_path()
    error_file_manager=FileManager(output_error_file_path)
    succ_file_manager=FileManager(output_succ_file_path)
    error_file_manager.intialize_headers_to_file_object(error_file_manager.get_error_headers(input_file_manager))
    succ_file_manager.intialize_headers_to_file_object(succ_file_manager.get_success_headers(input_file_manager))
    discount_coup_obj=DiscountCoupon()
    for each_row_dict in input_file_manager.read_data():
        passenger_obj=Passenger(each_row_dict)
        error_columns=passenger_validator_obj.validator(passenger_obj)
        if error_columns is not None:
            each_row_dict['Error']=error_columns+" Invalid"
            error_file_manager.write_data_dict(each_row_dict)
        else:
            each_row_dict['Discount_code']=discount_coup_obj.get_discount_code_FareClass(passenger_obj)
            succ_file_manager.write_data_dict(each_row_dict)





if __name__=="__main__":
    run_pipeline()








