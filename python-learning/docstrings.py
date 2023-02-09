import pickle

def square(n:int) -> float:
    """
    Returns the square of a number.

    Parameters:
        n (int): The number to square.
    
    Returns: 
        n * 2 (int): The square of n.
    """
    return n * 2

def multiplier(a:int, b:int) -> int:
  """Takes in two numbers, returns their product."""
  return a * b

def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum

class Person:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """

        print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)

def main() -> None:
    """
    Main function.
    """
    print(f'Square of 2: {square(2)}')
    print(print.__doc__)
    print(square.__doc__)
    print(pickle.__doc__)
    print(add_binary.__doc__)
    print(Person.__doc__)

if __name__ == '__main__':
  main()