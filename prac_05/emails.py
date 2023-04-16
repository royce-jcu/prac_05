def main():
    """Create dictionary to store the email and names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        if len(name) != 0:
            confirm = input(f"Is your name {name}? (Y/n) ")
            if confirm.lower() == "n":
                name = input("Name: ")
            email_to_name[email] = name
        else:
            print("Invalid email format")
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Return a name derived from user's email."""
    username = email.split("@")[0]

    if "." in username:
        first_name, last_name = username.split(".")
        name = " ".join([first_name,last_name]).title()
    else:
        name = username.title()

    return name


main()