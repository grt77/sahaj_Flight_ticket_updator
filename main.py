from src.Date_time_oper.DateOperations import DateOperations
from src.ConfigEnv import load_env_variables
from src.Files_oper.FileOperations import FileOperations
from src.Files_oper.FileManager import FileManager, ErrorFileManager, SucessFileManager
from src.passenger.Passenger import Passenger
from src.passenger.PassengerValidator import PassengerValidator
from src.discount_offer.DiscountCoupon import DiscountCoupon
from src.schema.SchemaValidation import SchemaValidation
import sys


def get_input_output_file_details():
    env_var = load_env_variables()
    file_format_date_obj = DateOperations(env_var['FILE_DATE_FORMAT'])
    file_format_date = file_format_date_obj.get_date_time_string()
    file_format_time_obj = DateOperations(env_var['FILE_TIME_FORMAT'])
    file_format_time = file_format_time_obj.get_date_time_string()
    input_file_obj = FileOperations(filename='', date_of_file=file_format_date, time_of_file=file_format_time)
    output_succ_file_obj = FileOperations(kind_of_file='success', date_of_file=file_format_date,
                                          time_of_file=file_format_time, filename='passenger_details',
                                          type_of_folder='OUTPUT_FOLDER')
    output_error_file_obj = FileOperations(kind_of_file='error', date_of_file=file_format_date,
                                           time_of_file=file_format_time, filename='passenger_details',
                                           type_of_folder='OUTPUT_FOLDER')
    input_file_path = input_file_obj.get_input_file_path()
    output_succ_file_path = output_succ_file_obj.generate_file_path()
    output_error_file_path = output_error_file_obj.generate_file_path()
    return {
        'input_file_path': input_file_path,
        'output_error_file_path': output_error_file_path,
        'output_success_file_path': output_succ_file_path
    }


def run_pipeline():
    file_path_dict = get_input_output_file_details()
    input_file_manager_obj = FileManager(file_path_dict['input_file_path'])
    if not (SchemaValidation(set(input_file_manager_obj.headers)).is_schemaColumns_valid()):
        sys.exit("Schema is not valid, please check with file")
    error_file_manager = ErrorFileManager(file_path_dict['input_file_path'], file_path_dict['output_error_file_path'])
    success_file_manager = SucessFileManager(file_path_dict['input_file_path'],
                                             file_path_dict['output_success_file_path'])
    passenger_validator_obj = PassengerValidator()
    discount_coup_obj = DiscountCoupon()
    for each_row_dict in input_file_manager_obj.read_data_dict_row_wise():
        passenger_obj = Passenger(each_row_dict)
        error_columns = passenger_validator_obj.validator(passenger_obj)
        if error_columns is not None:
            each_row_dict['Error'] = error_columns + " Invalid"
            error_file_manager.write_data_dict(each_row_dict)
        else:
            each_row_dict['Discount_code'] = discount_coup_obj.get_discount_code_FareClass(passenger_obj)
            success_file_manager.write_data_dict(each_row_dict)


run_pipeline()
