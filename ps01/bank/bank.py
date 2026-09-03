def main():

    balance = 500

    while True:
        try:
            
            print("\n------BANK ACCOUNT------\n\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit\n")
            choice = input("Choice: ")
            choice = int(choice)

            if choice > 4 or choice <= 0:
                print("enter valid choice\n")
                continue

            if choice == 1:
                print(f"Balance: {balance}\n")
                continue

            elif choice == 2:
                while True:
                    try:
                        dep = input("Deposit amount: ")
                        dep = int(dep)
                        if dep <= 0:
                            print("must be greater than 0\n")
                            continue
                        balance = balance + dep
                        print(f"New balance: {balance}\n")
                        break
                    except ValueError:
                        print("must be a whole number\n")
                        continue


            elif choice == 3:
                while True:
                    try:
                        withd = input("withdrawal amount: ")
                        withd = int(withd)
                        if withd < 0:
                            print("must be greater than 0\n")
                            continue
                        if withd > balance:
                            print("Isufficient balance\n")
                            continue
                        if withd % 20 != 0:
                            print("must be divisible by 20\n")
                            continue
                        balance = balance - withd
                        print(f"New balance: {balance}\n")
                        break
                    except ValueError:
                        print("must be a whole number\n")

                continue
            else:
                print("\nGoodbye")
                break
        except ValueError:
            print("must be a whole number\n")
main()