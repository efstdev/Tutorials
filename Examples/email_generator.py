u_name_first = str(input("Please provide your first name: "))
u_name_second = str(input("Please provide your last name: "))

# Joins the first and last name
u_name = u_name_first + u_name_second

# Adds 0 to the email ID
u_number = 0

u_email = f'{u_name}.{u_number}@someprovider.com'

used_mail = ['johndoe.0@someprovider.com', 'johndoe.1@someprovider.com']

# Checks if the email exists in the "used_mail" array
if u_email in used_mail:
    u_email = f'{u_name}.{u_number + len(used_mail)}@someprovider.com'
    print(u_email)
else: print(f'{u_name}.{u_number}@someprovider.com')

