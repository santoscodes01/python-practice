def main():
    while True:
        try:
            elec = input("Usage: ")
            elec = float(elec)

            if elec <= 0:
                print("Must be greater than 0")
                continue

            if elec <= 100:
                bill = elec * 0.12

            elif elec <= 300:
                remaining = elec - 100
                bill = (100 * 0.12) + (remaining * 0.15)

            else:
                remaining = elec - 300
                bill = (100 * 0.12) + (200 * 0.15) + (remaining * 0.20)

            print(f"Bill: ${bill:.2f}")
            break

        except ValueError:
            print("Must be a number")


main()