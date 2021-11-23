def get_username(first, last):
    s = first + "." + last
    return s.lower()

def main():
    first_name = input("ENTER YOUR FIRST NAME: ")
    last_name = input("ENTER YOUR LAST NAME: ")
    username = get_username(first_name, last_name)
    print("Your username is: " + username)

if __name__ == "__main__":
        main()