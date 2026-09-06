def main():


    while True:
        code = input("code: ")

        is_valid = code_validator(code)

        if is_valid == True:
            print("valid")
            break
        else:
            print("invalid")
            
def code_validator(code):
    
    has_digit = False
    has_upper = False
    has_lower = False

    for _ in code:
        if _ == " ": 
            return False

        if _.isdigit():
            has_digit = True

        if _.isupper():
            has_upper = True

        if _.islower():
            has_lower = True
            
    if len(code) != 8:
        return False

    if  has_digit and has_upper and has_lower:
        return True
        
    return False

main()