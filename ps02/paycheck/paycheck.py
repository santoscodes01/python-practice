def main():
    while True:
        try:
            hours = float(input("Hours worked: "))
            rate = float(input("Hourly rate: "))

            if hours <= 0 or rate <= 0:
                print("Values must be greater than 0.")
                continue

            break

        except ValueError:
            print("Must be a number.")

    pay = calculate_pay(hours, rate)
    print(f"Total pay: ${pay:.2f}")


def calculate_pay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = 40 * rate
        return regular_pay + overtime_pay

    return hours * rate


main()