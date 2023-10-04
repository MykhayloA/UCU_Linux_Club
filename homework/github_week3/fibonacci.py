"""
This is a Python script that takes a number as input from the
user and returns the corresponding number of Fibonacci terms.
It uses the formula for the nth term of the Fibonacci sequence
and functionally decomposes the calculations.
Fill in all the missing code in the functions and in main
"""
import math
import typing
def get_input() -> int:
    """Gets input from the user and returns it as an integer"""
    pass


def fibonacci_list(n: int) -> typing.List[int]:
    """Returns a list of the first n Fibonacci numbers"""
    pass


def fibonacci_single(nomer: int) -> int:

    """Returns the nth Fibonacci number"""
    return ((golden_section_num()**nomer) - ((-1 * golden_section_reciprocal())**nomer))/(5**(1/2))


def golden_section_num() -> float:
    """Returns the golden section number (capital Phi)"""
    return (5**(1/2) + 1)/2


def golden_section_reciprocal() -> float:
    """Returns the reciprocal of the golden section number (lowercase phi)"""
    lowercase_phi = golden_section_num - 1
    return lowercase_phi
    #pass


def power(num: int, n: int) -> int:
    """Raises num to the nth power"""
    num = num**n
    return num
    #pass


def sqrt(num: int) -> float:
    """Returns the square root of num"""
    return math.sqrt(num)


def main():
    """Main function"""

    # Bohdan
    # num = get_input()
    # print(n_fib_list = fibonacci_list(num))

    # Victor
    # print(n_fib_single = fibonacci_single(num))
    # print(capital_phi = golden_section_num())


    # Mykhailo part
    # print(lowercase_phi = golden_section_reciprocal())
    # print(power(num))
 

    # Mukhailo Bronytskyi part
    # print(sqrt(num))

    return


if __name__ == "__main__":
    main()