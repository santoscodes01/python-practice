def main():

    
            first = input("name: ")
            last = input("name: ")
            initials = make_initials(first, last)

            print(f"initials: {initials}")
            
        

def make_initials(first,last):

    first = first.strip().upper()[0]
    last = last.strip().upper()[0]
    initials = f"{first}.{last}"

    return initials

main()