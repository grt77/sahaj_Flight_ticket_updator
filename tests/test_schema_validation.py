import pytest
from src.schema.SchemaValidation import SchemaValidation
from test_data import test_data_schema_columns_validation

@pytest.mark.parametrize("input,expected_output", test_data_schema_columns_validation)
def test_schema_columns_validation(input, expected_output):
    schema_obj=SchemaValidation(set(input))
    assert schema_obj.is_schemaColumns_valid() == expected_output
