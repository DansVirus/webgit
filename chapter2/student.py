# Dilosi class stin python
class Student:
    """
    A class that represents a person with fisrt and last name
    Attributes:
    -fistname (str) : the firstname of the person
    -lastname (str) : the lastname of the person
    """

    def __init__(self, fisrtname, lastname):
        """
        Initialize a new instance of the Person class
        Args: 
        -fistname (str) : the firstname of the person
        -lastname (str) : the lastname of the person
        """
        self.firstname = fisrtname
        self.lastname = lastname
