def menu():
    """Displays opening window that calls itself again if a correct option
    is not entered. Will terminate the program if 3 is entered"""
    print("Menu\n-------------")
    print("1. Encoder\n2. Decoder\n3. Quit")


def FahimIslam_encoder(number):
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


def JonathonBrown_decoder(password):
    """takes the encoded string of numbers and returns the decoded string"""
    new_number = ''
    for character in password:
        holder = int(character) - 3
        if holder <= -1:
            holder += 10
        new_number += str(holder)
    return new_number


def main():
    while True:
        menu()  # prompts the menu to user
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            number = input("Please enter your password to encode: ")
            new_p = FahimIslam_encoder(number)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decode_password = JonathonBrown_decoder(new_p)  # uses output from encoder function
            print(f"The encoded password is {new_p}, and the original password is {decode_password}\n")
        elif option == 3:
            quit()
        else:
            menu()


if __name__ == "__main__":
    main()

