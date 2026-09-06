def main():

    while True:
        filename = input("file: ")
        new = format_filename(filename)
        
        if "." in new:
            print(new)
            break
        else:
            print("Invalid")
            
def format_filename(filename):

    
    filename = filename.lower().strip().replace(" ", "_")
    return filename
     

main()