from ..ConfigEnv import load_env_variables

class SchemaValidation:
    def __init__(self,schemaColumns):
        self.file_schema_columns=schemaColumns
        self.env_var=load_env_variables()
        self.expected_schema=set(eval(self.env_var['VALID_SCHEMA_COLUMNS']))

    def is_schemaColumns_valid(self):
        if len(self.expected_schema-self.file_schema_columns)==0:
            return True
        else:
            return  False