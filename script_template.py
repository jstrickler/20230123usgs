"""
This is the doc string for the module/script.
"""
import sys

# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    function1()

# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """
    print("this is function1()")

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
