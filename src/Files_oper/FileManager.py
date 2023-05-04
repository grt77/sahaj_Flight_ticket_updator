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

    def __init__(self,file_path,headers=None,mode='a+'):
        self.file_path=file_path
        self.mode=mode


    def intialize_headers_to_file_object(self,headers):
        self.headers = headers
        self.write_data(headers)


    def write_data(self,data):
        print("data",data)
        with open(self.file_path,'a+',newline='') as file:
            writer_obj=csv.writer(file)
            writer_obj.writerow(data)

    def write_data_dict(self, data_dict):
        with open(self.file_path, 'a+', newline='') as file:
            writer_obj = csv.DictWriter(file,fieldnames=self.headers)
            writer_obj.writerow(data_dict)


    def read_data(self):
        try:
            with open(self.file_path,mode='r') as read_file:
                csv_reader=csv.DictReader(read_file)
                for row in csv_reader:
                    yield row
        except Exception as err:
            print(err)

    def get_headers_file(self):
        try:
            with open(self.file_path, mode='r') as read_file:
                csv_reader=csv.DictReader(read_file)
                headers=csv_reader.fieldnames
            return headers
        except Exception as err:
            print(err)

    def get_error_headers(self,FileManager):
        error_file_headers=list(FileManager.get_headers_file())
        error_file_headers.append('Error')
        return error_file_headers


    def get_success_headers(self,FileManager):
        succ_file_headers = list(FileManager.get_headers_file())
        succ_file_headers.append('Discount_code')
        return succ_file_headers

