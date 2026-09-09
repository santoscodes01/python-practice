def main():
    while True:
        name = input("Name: ")
        formatted = format_name(name)

        if formatted is False:
            print("Enter at least a first and last name.")
        else:
            print(f"Formatted: {formatted}")
            break


def format_name(name):
    parts = name.split()

    if len(parts) < 2:
        return False

    formatted_parts = []

    for part in parts:
        formatted_parts.append(part.lower().title())

    return " ".join(formatted_parts)


main()