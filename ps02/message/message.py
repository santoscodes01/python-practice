def main():
    while True:
        message = input("message: ")

        is_valid = validate_message(message)

        if is_valid:
            print("valid")
            break
        else:
            print("not valid")

def validate_message(message):

    has_digit = False
    has_upper = False
    has_lower = False

    if len(message) < 10 or len(message) > 40:
        return False

    for _ in message:
        if _.isdigit():
            has_digit = True
        if _.isupper():
            has_upper = True
        if _.islower():
            has_lower = True

    if has_digit and has_upper and has_lower and message[-1] in ".!?":
        return True

    
    return False

main()