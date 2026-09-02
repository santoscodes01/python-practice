def main():


    from random import randint
    x = randint(1,100)
    count = 0
    while True:
        try:
            
            guess = input("Guess: ")
            guess = int(guess)
            if guess > 100 or guess < 1:
                print("must be within range 1 -100")
                continue
            if guess > x:
                print("too high")
                count += 1
                continue
            elif guess < x:
                print("too low")
                count += 1
                continue
            else:
                count += 1
                print(f"correct\n tries:", count)
                break

        except ValueError:
             print("must be a number")
             continue
    

main()