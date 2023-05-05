import csv

'''
FileManager.intialize_headers()->
This is going to helpful to intializing the headers to a file , which we passed file path to a class for object creation


FileManager.write_data()->
Write the data to file with message provided as an argument 

FileManager.write_data_dict()->
helpful for writing to a csv file with dict as a message 

FileManager.read_data()->
helpful for reading the csvfile data in form of dict


'''




class FileManager:
    def __init__(self, file_path):
        self.input_file_path = file_path
        self.headers = self.get_file_headers()

    def get_file_headers(self):
        try:
            with open(self.input_file_path, mode='r') as read_file:
                csv_reader = csv.DictReader(read_file)
                headers = csv_reader.fieldnames
            return headers
        except Exception as err:
            print(err)

    def read_data_dict_row_wise(self):
        try:
            with open(self.input_file_path, mode='r') as read_file:
                csv_reader = csv.DictReader(read_file)
                for row in csv_reader:
                    yield row
        except Exception as err:
            print(err)

    def write_data_dict(self, data_dict):
        with open(self.input_file_path, 'a+', newline='') as file:
            writer_obj = csv.DictWriter(file, fieldnames=self.headers)
            writer_obj.writerow(data_dict)

    def write_data(self, data):
        print("data", data)
        with open(self.input_file_path, 'a+', newline='') as file:
            writer_obj = csv.writer(file)
            writer_obj.writerow(data)

    def intialize_headers_to_file_object(self):
        self.write_data(self.headers)


class ErrorFileManager(FileManager):
    def __init__(self, input_file_path, error_file_path,intialize_headers=True):
        super().__init__(input_file_path)
        self.input_file_path = error_file_path
        self.headers.append('Error')
        if intialize_headers:
            self.intialize_headers_to_file_object()


class SucessFileManager(FileManager):
    def __init__(self,input_file_path,success_file_path,intialize_headers=True):
        super().__init__(input_file_path)
        self.input_file_path=success_file_path
        self.headers.append('Discount_code')
        if intialize_headers:
            self.intialize_headers_to_file_object()


