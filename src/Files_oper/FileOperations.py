from datetime import datetime
from ..ConfigEnv import load_env_variables
import os

'''
FileOperations.generate_dir_path()->
helpful get the directory path while using the arguments which we provided 

FileOperations.generate_file_path()->
helpful for generating the file path for what ever type of file u want 

'''


class FileOperations:
    def __init__(self,filename,date_of_file,time_of_file,type_of_folder='',kind_of_file=None):
        self.folder_type=type_of_folder
        self.filename=filename
        self.date=date_of_file
        self.kind_of_file=kind_of_file
        self.env_args=load_env_variables()
        self.time_of_file=time_of_file

    def generate_dir_path(self,want_to_create=True):
        folder_name = self.env_args[self.folder_type]
        directory_path = os.path.join(folder_name, self.date[0:4], self.date[4:6], self.date[6:], self.kind_of_file)
        if want_to_create:
            try:
                os.makedirs(directory_path)
            except FileExistsError:
                print("Dir already exists")
        return directory_path

    def generate_file_path(self):
        dir_path=self.generate_dir_path(True)
        file_path=os.path.join(dir_path,self.filename+"_"+str(self.time_of_file)+".csv")
        return file_path

    def get_input_file_path(self):
        input_file_path=os.path.join(self.env_args['INPUT_FOLDER'],self.env_args['INPUT_FILE_FORMAT']+self.date+".csv")
        return input_file_path



