def menu():
    """Displays opening window that calls itself again if a correct option
    is not entered. Will terminate the program if 3 is entered"""
    print("Menu\n-------------")
    print("1. Encoder\n2. Decoder\n3. Quit")


def JonathonBrown_encoder(number):
    """Taces a string of integers, and adds 3 to each int % 10 so only single
    digits and returns as a string of the effected ints"""
    number = number
    encoder = []
    for a in range(len(number)):
        encoder.append(number[a])
    encoder = [int(b) for b in encoder]

    number = ''
    for c in encoder:
        if c in range(0, 7):
            c += 3
            number += str(c)
        elif c == 7:
            number += '0'
        elif c == 8:
            number += '1'
        elif c == 9:
            number += '2'
    number = number
    return number


def FahimIslam_decoder(password):
    # takes the return statement from encoder function and returns the decoded password (original password)
    new_string = ""

    for char in password:
        number = int(char)

        if number == 0:
            new_num = 7
        elif number == 1:
            new_num = 8
        elif number == 2:
            new_num = 9
        else:
            new_num = number - 3  # for each character, the number will be subtracted by 3

        half_str = str(new_num)

        new_string += half_str

    return new_string


def main():
    while True:
        menu()  # prompts the menu to user
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            number = input("Please enter your password to encode: ")
            new_p = JonathonBrown_encoder(number)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decode_password = FahimIslam_decoder(new_p)  # uses output from encoder function
            print(f"The encoded password is {new_p}, and the original password is {decode_password}\n")
        elif option == 3:
            quit()
        else:
            menu()


if __name__ == "__main__":
    main()

