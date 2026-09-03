def main():

    
    attempt = 3
    password = "python123"
    while attempt > 0:
        tri = input("password: ") 
        if tri == password:
            print("Access granted.")
            break
        else:
            attempt -= 1
            if attempt > 1:
                print(f"Incorrect. {attempt} attempts remaining.")
            elif attempt == 1:
                print(f"Icorrect. {attempt} attempt remaining.")
            else:
                print("Account locked.")


main()