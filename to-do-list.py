mylist = []
def remove_validation(number:str, list:list):
    while True:
        if number.isdigit() and int(number) <= len(list) and int(number) >= 0:
            return int(number)
        else:
            print("Please pick a number on the list")
            number = input("> ")
    
        
def main():
    while True:
        print("List of things to do:")
        for index, item in enumerate(mylist):
            print(f"{index}. {item}")
        choice = input("would you like to add an item [1], delete an item [2], or are you done [3]? ")
        if choice == "1":
            text = input("What would you like to add to the list?\n> ")
            mylist.append(text)
        elif choice == "2":
            remove = input("Please insert the number of the item you want deleted.\n> ")
            remove = remove_validation(remove, mylist)
            mylist.pop(remove)
            pass
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("\nPlease pick a valid option\n")

if __name__=="__main__":
    main()

        