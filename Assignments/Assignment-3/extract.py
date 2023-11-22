import re
import csv

def extract_contacts(input_text):
    # Regular expression pattern for extracting mobile numbers
    phone_pattern = re.compile(r'\b\d{10}\b')

    # Regular expression pattern for extracting email addresses
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Find all matches in the input text
    phone_numbers = phone_pattern.findall(input_text)
    email_addresses = email_pattern.findall(input_text)

    return phone_numbers, email_addresses

def main():
    # Read data from the input text file
    with open("Assignments/Assignment-3/data.txt", 'r') as file:
        input_data = file.read()

    # Extract mobile numbers and email addresses
    phone_numbers, email_addresses = extract_contacts(input_data)

    # Write the results to a new text file
    with open('contacts.txt', 'w') as output_file:
        output_file.write('Mobile Numbers:\n')
        output_file.write('\n'.join(phone_numbers))
        output_file.write('\n\nEmail Addresses:\n')
        output_file.write('\n'.join(email_addresses))

    # Alternatively, you can write the results to a CSV file
    with open('contacts.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Mobile Numbers', 'Email Addresses'])
        writer.writerows(zip(phone_numbers, email_addresses))

if __name__ == "__main__":
    main()
