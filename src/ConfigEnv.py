import os
from dotenv import load_dotenv

'''
this is useful for returning env variables 

'''


def load_env_variables():
    load_dotenv()
    env_var={}
    for key,value in os.environ.items():
        env_var[key]=value
    return env_var




