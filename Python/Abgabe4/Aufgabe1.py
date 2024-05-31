class Complex:
    """
    A class to represent a complex number.
    
    Attributes
    ----------
    real : int
        The real part of the complex number.
    imag : int
        The imaginary part of the complex number.
    zeichen : str
        The symbol used for the imaginary unit, either 'i' or 'j'. Defaults to 'i'.
    
    Methods
    -------
    __init__(real: int = 0, imag: int = 0, zeichen: str = 'i'):
        Initializes the complex number with the given real and imaginary parts.
        
    disp():
        Displays the complex number in the format 'a+bi' or 'a+bj'.
        
    __add__(obj2: Complex) -> Complex:
        Adds two complex numbers and returns the result as a new Complex object.
        
    __str__() -> str:
        Returns a string representation of the complex number.
    """

    def __init__(self, real: int = 0, imag: int = 0, zeichen: str = 'i'):
        """
        Initializes the Complex number with real and imaginary parts.
        
        Parameters
        ----------
        real : int, optional
            The real part of the complex number (default is 0).
        imag : int, optional
            The imaginary part of the complex number (default is 0).
        zeichen : str, optional
            The symbol for the imaginary unit, either 'i' or 'j' (default is 'i').
            If any other value is provided, it defaults to 'i'.
        """
        self.real = real
        self.imag = imag
        if zeichen == 'j':
            self.zeichen = zeichen
        else:
            self.zeichen = 'i'

    def disp(self):
        """
        Displays the complex number in a readable format 'a+bi' or 'a+bj'.
        
        Returns
        -------
        str
            A string representing the complex number.
        """
        cpxStr = "{0}{1:+}{2}".format(self.real, self.imag, self.zeichen)
        print(cpxStr)
        return cpxStr

    def __add__(self, obj2: 'Complex') -> 'Complex':
        """
        Adds two Complex numbers.
        
        Parameters
        ----------
        obj2 : Complex
            The second complex number to be added.
        
        Returns
        -------
        Complex
            A new Complex object which is the sum of self and obj2.
        """
        return Complex(real=(self.real + obj2.real), imag=(self.imag + obj2.imag))

    def __str__(self) -> str:
        """
        Returns the string representation of the Complex number.
        
        Returns
        -------
        str
            A string representing the complex number in the format 'a+bi' or 'a+bj'.
        """
        return "{0}{1:+}{2}".format(self.real, self.imag, self.zeichen)


if __name__ == "__main__":
    a = Complex(real = 5)
    a.disp()
    b = Complex(real= -10, imag = -5, zeichen = 'j')
    b.disp()
    c = a + b
    c.disp()