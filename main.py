full_email_address = str(input('Enter your email address: ')).strip()

username_of_email = full_email_address[:full_email_address.index('@')]
domain_of_email = full_email_address[full_email_address.index('@') + 1:]

print(f'The username of the email is {username_of_email} and the domain is {domain_of_email}.')