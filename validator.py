import re
import datetime
from urllib.parse import urlparse

class DataValidator():
    """
    A class to validate email,phone number, date and url data
    
    """
    def __init__(self):
      pass


#Validate an email
    def validate_email(self):   
        
        """
        Validates an email address by checking the prefix and domain.

        Args:
            email (str): The email address to validate.

        Returns:
            tuple: A tuple containing (bool, str), where the bool indicates if the email is valid,
                and the str contains a message describing the validation result.
        """
            
        email = input("Enter email for validation: ")
        
        #Splits the email into prefix and domain (example@gmal.com: example = prefix; gmail.com = domain)
        parts = email.split('@')
        if len(parts) != 2 :
            return False, "Invalid email format (missing or multiple @ symbols)."
        
        prefix, domain = parts
        
        #validate prefix
        if prefix.startswith (".") or '..' in prefix or ' ' in prefix:
            return False, "Invalid email prefix \n (Ensure the email doesn't start with a fullstop, or space in between, or consecutive full stops)"
        
        
        #validate domain
        valid_domains=["gmail.com","yahoo.com","outlook.com","hotmail.com","icloud.com","msn.com","aol.com"]
        if domain not in valid_domains:
            return False, f"Invalid email domain. Valid domains are: {', '.join(valid_domains)}"
        
        return True, "Email is valid"



#Validate phone number (Nigeria e.g 08033458223)
    def validate_phone(self):
        try:
            phone = input("Enter phone number: ")
            # Attempt to convert to int to check for non-numeric input
            int(phone)
        except ValueError:
            return False, "Invalid input type. Enter numbers only."

        pattern = r"^0\d{10}$"
        if re.match(pattern, phone):
            return True, "The number is valid"
        else:
            return False, "The number is invalid"

      
#Validate a date
    def validate_date(self,year,month,day):
        """Method to check if a date is valid

        Args:
            year (int): The year
            month (int): the month
            day (int): the day

        Returns:
            bool: True if valid, False if invalid
        """
        try:
            datetime.date(year,month,day)
            return True, "Date is valid"
        except ValueError:
            return False, "Date is invalid"
        


#Validate a URL
    def validate_url(self):
        url = input("Enter URL: ")
        try:
            result = urlparse(url)
            if all([result.scheme, result.netloc]):
                regex = re.compile(
                    r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
                )
                if regex.match(url):
                    return True, "Valid URL"
                else:
                    return False, "Invalid URL"
            else:
                return False, "Invalid URL"
        except ValueError:
            return False, "Invalid URL"
    
   
   
   
def run_data_validator():
    
    validator = DataValidator()
    
    while True:
                
        print("\n Data Validator Menu: ")
        print("(A): Validate Email")
        print("(B): Validate Phone Number")
        print("(C): Validate Date")
        print("(D): Validate URL")
        print("(E): Exit Data Validator ")
    
        choice = input ("PICK WHAT YOU WANT TO VALIDATE (A/B/C/D): ").upper()
        
        if choice == "A":
            is_valid, message = validator.validate_email()
            print(message)
        elif choice == "B":
            is_valid, message = validator.validate_phone()
            print(message)
        elif choice == "C":
            try:
                year = int(input("Enter the year: "))
                month = int(input("Enter the month (1-12): "))
                day = int(input("Enter the day: "))
            except ValueError:
                print("Invalid input for year, month, or day. Please enter numbers.")
                continue  # Go back to the menu
            is_valid, message = validator.validate_date(year, month, day)
            print(message)
        elif choice == "D":
            is_valid, message = validator.validate_url()
            print(message)
        elif choice == "E":
            print("Thank you for using your service \n Exiting Data Validator ...")
            break
        else:
            print("Invalid input, Enter either A/B/C/D/E")
   
   
if __name__ == "__main__":
    run_data_validator()