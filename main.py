mylist = []
def main():
    while True:
        print("List of things to do:")
        for index, item in enumerate(mylist):
            print(f"{index}. {item}")
        choice = input("would you like to add an item [1] or are you done [2]? ")
        if choice == "1":
            text = input("What would you like to add to the list?\n> ")
            mylist.append(text)
        elif choice == "2":
            print("Goodbye")
            break
        else:
            print("\nPlease pick a valid option\n")

if __name__=="__main__":
    main()

        