def main():


    bal = 500

    while True:
        try:
            withdraw = input("withdrawal amount: ")
            withdraw = int(withdraw)
            if withdraw <= 0:
                print("Amount must be greater than 0")
                continue
            if withdraw > 500:
                print("Insufficient funds")
                continue
            if withdraw % 20 != 0:  
                print("amount must be multiple of 20")
                continue
            new = bal - withdraw
            print(f"wirhdrew: {withdraw}\nRemaining balance: {new}")
            break
        except ValueError:
            print("must be whole dollar amount")






main()