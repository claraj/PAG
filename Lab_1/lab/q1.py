# Question 1

def main():

    # You don't need to modify this function.

    a = input('Enter one number')
    b = input('Enter another number')

    compare = which_number_is_larger(a, b)

    if compare == 'same':
        print('The two numbers are the same')
    else:
        print('The %s number is larger' % compare)



def which_number_is_larger(first, second):

    # TODO if the first number is larger, return the string 'first'
    # TODO if the second number is larger, return the string 'second'
    # TODO if the numbers are the same, return the string 'same'

    return   # TODO replace this with your code


# You don't need to modify this code.
if __name__ == "__main__":
    main()
