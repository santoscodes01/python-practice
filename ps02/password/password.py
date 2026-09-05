def main():
    password = input("Enter password: ")
    validate = validate_password(password)

    print(validate)


def validate_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for character in password:
        if character == " ":
            return False

        if character.isupper():
            has_upper = True

        if character.islower():
            has_lower = True

        if character.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return True

    return False


main()