def main():
    while True:
        email = input("email: ")
        email = clean_email(email)
        if email:
            print(f"{email}")
            break
        else:
            print ("not valid")
            continue
        

def clean_email(email):

    email = email.strip()
    email = email.lower()
    for _ in email:
         if _ == " ":
            print("spaces")
            return False
   
    if "." not in email or "@" not in email:
        return False
    return email
    


main()