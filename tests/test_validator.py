import pytest
from ..validator import DataValidator


#test to check if date is being validated
def test_validate_date_valid(monkeypatch):
    """Test for valid date input."""
    validator = DataValidator()
    # Test valid date
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '2024')
        year = int(input("Enter the year: "))
        m.setattr('builtins.input', lambda _: '10')
        month = int(input("Enter the month (1-12): "))
        m.setattr('builtins.input', lambda _: '26')
        day = int(input("Enter the day: "))
        assert validator.validate_date(year, month, day) == (True, "Date is valid")


#test to check for proper error message with invalid date input
def test_validate_date_invalid(monkeypatch):
    """Test for invalid date input."""
    validator = DataValidator()
    # Test invalid date (Feb 30)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '2023')
        year = int(input("Enter the year: "))
        m.setattr('builtins.input', lambda _: '2')
        month = int(input("Enter the month (1-12): "))
        m.setattr('builtins.input', lambda _: '30')
        day = int(input("Enter the day: "))
        assert validator.validate_date(year,month,day) == (False, "Date is invalid")


#test to check for proper error message with invalid month number
def test_validate_invalid_month_range(monkeypatch):
    """Test for invalid month number."""
    validator = DataValidator()
    # Test invalid month (13)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '2023')
        year = int(input("Enter the year: "))
        m.setattr('builtins.input', lambda _: '13')
        month = int(input("Enter the month (1-12): "))
        m.setattr('builtins.input', lambda _: '10')
        day = int(input("Enter the day: "))
        assert validator.validate_date(year,month,day) == (False, "Date is invalid")


#test to check for proper error message with invalid day number
def test_validate_invalid_day_range(monkeypatch):
    """Test for invalid day number."""
    validator = DataValidator()
    # Test invalid day (32)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '2023')
        year = int(input("Enter the year: "))
        m.setattr('builtins.input', lambda _: '10')
        month = int(input("Enter the month (1-12): "))
        m.setattr('builtins.input', lambda _: '32')
        day = int(input("Enter the day: "))
        assert validator.validate_date(year,month,day) == (False, "Date is invalid")



#test to check if email is being validated
def test_validate_email(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: 'test@gmail.com')
        is_valid, message = validator.validate_email()
        assert is_valid is True
        assert message == "Email is valid"
                


#test to check for proper error message with invalid email 
def test_validate_invalid_email(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: 'testgmail.com')
        is_valid, message = validator.validate_email()
        assert is_valid is False
        assert message == "Invalid email format (missing or multiple @ symbols)."



#test to check for proper error message with invalid email prefix
def test_validate_invalid_email_prefix(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '.test@gmail.com')
        is_valid, message = validator.validate_email()
        assert is_valid is False
        assert message == "Invalid email prefix \n (Ensure the email doesn't start with a fullstop, or space in between, or consecutive full stops)"


#test to check for proper error message with invalid email domain
def test_validate_invalid_email_domain(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: 'test@youmail.com')
        is_valid, message = validator.validate_email()
        assert is_valid is False
        assert message == "Invalid email domain. Valid domains are: gmail.com, yahoo.com, outlook.com, hotmail.com, icloud.com, msn.com, aol.com"


#test to check if phone number is being validated
def test_validate_phone(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '07064284299')
        is_valid, message = validator.validate_phone()
        assert is_valid is True
        assert message == "The number is valid"

#test to check for proper error message with invalid phone number
def test_validate_invalid_phone(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '070642842997')
        is_valid, message = validator.validate_phone()
        assert is_valid is False
        assert message == "The number is invalid"

#test to check for proper error message with invalid phone number type
def test_validate_invalid_phone_type(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: 'number')
        is_valid, message = validator.validate_phone()
        assert is_valid is False
        assert message == "Invalid input type. Enter numbers only."

#test to check if url is being validated
def test_validate_url(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: 'https://www.example.com')
        is_valid, message = validator.validate_url()
        assert is_valid is True
        assert message == "Valid URL"

#test to check for proper error message with invalid url
def test_validate_invalid_url(monkeypatch):
    validator = DataValidator()
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: 'htt://www.examplecom')
        is_valid, message = validator.validate_url()
        assert is_valid is False
        assert message == "Invalid URL"