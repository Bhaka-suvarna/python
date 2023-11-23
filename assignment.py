import re

def extract_contacts(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Regular expression patterns for extracting mobile numbers and email addresses
    phone_pattern = re.compile(r'\b\d{10}\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Extract mobile numbers
    phone_numbers = phone_pattern.findall(data)

    # Extract email addresses
    email_addresses = email_pattern.findall(data)

    return phone_numbers, email_addresses

if __name__ == "__main__":
    file_path = "data.txt"
    phone_numbers, email_addresses = extract_contacts(file_path)
    print("mobile_numbers:")
    for number in phone_numbers:
        print(number)
    print("email_addresses:")
    for email in email_addresses:
        print(email)