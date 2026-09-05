def main():
    
    while True:
        try:
            hours = float(input("hours parked: "))
            if hours <= 0:
                continue
            break
        except ValueError:
            continue
    while True:
        has_pass = input("Pass: ").lower()
        if has_pass == "yes" or has_pass == "no":
            break
    cost = calculate_parking(hours,has_pass)
    print(f"fee: ${cost:.2f}")


def calculate_parking(hours,has_pass):
    if hours <= 2:
        price = 5
    else:
        remainder_hours = hours - 2
        price = remainder_hours * 3 + 5
        if price > 25:
            price = 25
    if has_pass == "yes":
        price -= 5
    if price < 0:
        price = 0
    return price


main()