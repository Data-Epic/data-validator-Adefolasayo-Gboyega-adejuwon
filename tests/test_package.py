import sys
print(sys.executable)
from datavalidator_Adefolasayo.validator import DataValidator
import datavalidator_Adefolasayo

def test_package():
    validator = DataValidator()

    # Test email validation
    valid_email, email_message = validator.validate_email()
    print(f"Email: {email_message}")

    # Test phone validation
    valid_phone, phone_message = validator.validate_phone()
    print(f"Phone: {phone_message}")

    # Test date validation
    valid_date, date_message = validator.validate_date(2024, 10, 27)
    print(f"Date: {date_message}")

    # Test URL validation
    valid_url, url_message = validator.validate_url()
    print(f"URL: {url_message}")

if __name__ == "__main__":
    test_package()