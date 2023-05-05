from test_data import test_data_email_validation, test_data_phone_number_validation, test_data_fare_class_validation , test_data_pnr_validation,test_data_book_cabin_validation
import pytest
from src.passenger.PassengerValidator import PassengerValidator

passenger_validator_obj = PassengerValidator()


@pytest.mark.parametrize("input,expected_output", test_data_email_validation)
def test_email_validation(input, expected_output):
    assert passenger_validator_obj.is_email_valid(input) == expected_output


@pytest.mark.parametrize("input,expected_output", test_data_phone_number_validation)
def test_phone_number_validation(input, expected_output):
    assert passenger_validator_obj.is_phone_number_valid(input) == expected_output


@pytest.mark.parametrize("input,expected_output", test_data_fare_class_validation)
def test_fare_class_validation(input, expected_output):
    assert passenger_validator_obj.is_fare_class_valid(input) == expected_output


@pytest.mark.parametrize("input,expected_output", test_data_pnr_validation)
def test_pnr_validation(input, expected_output):
    assert passenger_validator_obj.is_pnr_valid(input) == expected_output

@pytest.mark.parametrize("input,expected_output", test_data_book_cabin_validation)
def test_book_cabin_validation(input, expected_output):
    assert passenger_validator_obj.is_booked_cabin_valid(input) == expected_output
