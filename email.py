def main():
    email_to_name = {}
    email = input("Email : ")
    while email != "":
        name = name_from_email(email)
        confirm_name = input(f"Is your name {name}? (Type Y/N)")
        if confirm_name.upper() != "Y" and confirm_name != "":
            name = input("Enter your name : ")
        email_to_name[email]=name
        email = input("Email : ")

    for email,name in email_to_name.items():
        print(f"{name} {email}.")

def name_from_email(email):
    at_symbols = email.split('@')[0]
    dots_symbols = at_symbols.split('.')
    name = "".join(dots_symbols).title()
    return name

main()