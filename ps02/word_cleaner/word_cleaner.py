def main():

    while True:
        word = input("word: ")
        
        word = clean_word(word)
        if not word:
            continue
        print(f"cleaned: {word}\nfirst: {word[0]}\nlast: {word[-1]}")

        
 

def clean_word(word):
    word = word.strip()
    word = word.lower()
    if len(word) < 3:
        return False
    for letter in word:
        if letter in " ":
            return False
    
    return word


main()




