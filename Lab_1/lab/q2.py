# Question 2

def main():

    # You don't need to modify this function.

    name = input('Enter your name')

    longer_than_6_letters = is_longer_than_6_letters(name)

    if longer_than_6_letters:
        print('Your name is longer than 6 letters.')
    else:
        print('Your name is 6 letters or shorter')


    shout_name = shout(name)

    print('This program is excited to see you, ', shout_name)




def is_longer_than_6_letters(name):

    # TODO return True if the name is longer than 6 letters
    # TODO return False if the name is 6 letters or shorter

    return  # TODO replace this with your code


def shout(name):

    # TODO return the name in uppercase with !!! at the end.
    # Example: if the name is 'Beyonce' then return 'BEYONCE!!!'

    return  'BEYONCE!!!'# TODO replace this with your code


# You don't need to modify this code.
if __name__ == "__main__":
    main()