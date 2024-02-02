import random
import string


def random_letter():
    # picking one random letter
    letters = string.ascii_letters
    return random.choice(letters)


def random_char():
    # picking one random character
    chars = string.punctuation + string.digits
    return random.choice(chars)


print("//* Random password generator *//")
while True:
    length = input("Give password length (8-32) or press 'q' to quit: ")
    if length == 'q':
        print("Exiting the program.")
        break
    elif length.isdigit() and 8 <= int(length) <= 32:
        password = ''

        # randomizing pick between letter and character
        for i in range(int(length)):
            if random.randint(1, 2) == 1:
                password += random_letter()
            else:
                password += random_char()
        print("Your password: ")
        print(password)

        # save to a file option
        while True:
            save_option = input("Do you want to save the password to a file? (y/n): ")
            if save_option == 'q':
                print("Exiting the program.")
                break
            elif save_option.lower() == 'y':
                file_name = "password_generator.txt"
                with open(file_name, "a") as file:
                    file.write(password + "\n")
                print(f"Password saved in {file_name}")
                break
            elif save_option.lower() == 'n':
                print("Password not saved.")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        break
    else:
        print("Please give a number between 8 and 32.")
