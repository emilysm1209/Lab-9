def decode(password):
    decoded_password = ''.join(str((int(char) - 3) % 10) for char in password)
    return decoded_password

def encode(password):
    encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password

if __name__ == "__main__":

    while True:
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        user_choice = input("Please enter an option: ")

        if user_choice == "1":
            password = input("Please enter the password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")

        elif user_choice == "2":
            decoded_pass = decode(encoded_pass)
            print("The encoded password is " + encoded_pass + ", and the original password is", decoded_pass + ".")

        elif user_choice == "3":
            print()
