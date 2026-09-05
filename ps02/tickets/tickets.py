def main():


    while True:
        try:
            age = int(input("Age: "))
            if age > 0:
                break
        except ValueError:
            continue
    
    while True:
        day = (input("weekday or weekend: ")).lower()
        if day == "weekday" or day == "weekend":
            break

    ticket = calculate_ticket(age,day)
    print(F"Tickets = ${ticket:.2f}")
        

def calculate_ticket(age,day):
 
    if day == "weekend":
        extra = 3
    else:
        extra = 0
    
    if age < 13:
        cost = 8
    elif 13 <= age <= 64:
        cost = 12
    else:
        cost = 9
    
    return cost + extra
main()