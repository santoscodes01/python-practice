def main():

     while True:
        try:
             weight = input("weight: ")
             weight = float(weight)
             if weight <= 0:
                print("Weight must be greater than 0")
                continue
             if weight <= 2:
                print("shipping cost: $5")
                break
             elif weight <= 5:
                print("shipping cost: $8")
                break
             elif weight <= 10:
                print("shipping cost: $12")
                break
             else:
                print("shipping cost: $20")
                break
        except ValueError:
            print("Please enter a number")
            continue


main()   