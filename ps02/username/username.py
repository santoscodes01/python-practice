def main():

    while True:
        username = input("username: ").lower().strip()
        

        if validate_username(username) == True:
             break
        else:
            print("not valid")
            continue
    print(f"{username}")


def validate_username(username):


     

    if len(username) < 5 or len(username) > 15:
        return False
    for _ in username:
        if _ == " ":
            return False
    if username.replace("_", "").isalnum() == True:
        return True
    return False


main()