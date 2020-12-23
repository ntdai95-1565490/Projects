class GreatestCommonDivisor:
    """Attributes:
    - a: integer
    - b: integer"""

    # Initializing a and b integers
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # This is the main function to find the greatest common divisor of a and b
    def greatest_common_divisor(self):
        """Calculates the remainder of a divided by b and then using recursion it calls itself by passing b and the remainder as its
        new arguments"""
        # Calculating the remainder
        r = self.a % self.b
    
        # Base condition: if the remainder is 0, then that means a is divisible by b, so b is the greatest common divisor since b 
        # is the greatest factorial of b. Then, we need to return the absolute value of b because b could be negative as well but 
        # we only care about positive values
        if r == 0:
            return abs(self.b)
        # Else, it will call itself by passing b and the remainder as its new arguments
        else:
            # Using recursion, creating the instance of the GreatestCommonDivisor class
            instance_of_GreatestCommonDivisor = GreatestCommonDivisor(self.b, r)
            return instance_of_GreatestCommonDivisor.greatest_common_divisor()

class Fraction:
    """Attributes:
    - numerator: integer
    - denominator: integer"""

    # Initializing the numerator and the denominator
    def __init__(self, numerator, denominator):
        # We already set the numerator and the denominator in our main class to be integers and the denominators to not be 0, but for 
        # other uses, we can check it again below
        if isinstance(numerator, int) == True and isinstance(denominator, int) == True and denominator != 0:
            # If both the numerator and the denominator is negative, then simplify it right away
            if numerator < 0 and denominator < 0:
                self.numerator = abs(numerator)
                self.denominator = abs(denominator)
            else:
                self.numerator = numerator
                self.denominator = denominator

    # Overriding the addition method
    def __add__(self, other):
        """Calculated the resulting numerator and denominator when the two fractions are adding up"""
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        return self

    # Overriding the subtraction method
    def __sub__(self, other):
        """Calculated the resulting numerator and denominator when the two fractions are subtracting from each other"""
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        return self

    # Overriding the multiplication method
    def __mul__(self, other):
        """Calculated the resulting numerator and denominator when the two fractions are multiplied with each other"""
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        return self

    # Overriding the division method
    def __truediv__(self, other):
        """Calculated the resulting numerator and denominator when the two fractions are divided by each other"""
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        return self

    # Overriding the greater than method
    def __gt__(self, other):
        """Overrriding the greater function"""
        if self.numerator/self.denominator > other.numerator/other.denominator:
            # First fraction is greater than the second fraction.
            return True
        else:
            # First fraction is not greater than the second fraction."
            return False

    # Overriding the equal to method
    def __eq__(self, other):
        """Overriding the equal function"""
        if self.numerator/self.denominator == other.numerator/other.denominator:
            # The two fractions are equal.
            return True
        else:
            # # The two fractions are not equal.
            return False

    # Overriding the less than method
    def __lt__(self, other):
        """Overrriding the lower function"""
        if self.numerator/self.denominator < other.numerator/other.denominator:
            # First fraction is smaller than the second fraction.
            return True
        else:
            # First fraction is not smaller than the second fraction.
            return False

    # Overriding the string method
    def __str__(self):
        """Find out the resulting correct fraction form"""
        # Calling the Greatest Common Divisor function from the module of Fraction_gcd
        instance_of_GreatestCommonDivisor = GreatestCommonDivisor(self.numerator , self.denominator)
        greatest_common_divisor = instance_of_GreatestCommonDivisor.greatest_common_divisor()
        # Checks if the greatest common divisor is not 1, then the fraction can be further simplify it
        if greatest_common_divisor != 1:
            self.numerator = int(self.numerator / greatest_common_divisor)
            self.denominator = int(self.denominator / greatest_common_divisor)
        # If the denominator is 1 or -1, then the fraction is equal to the positive or negative numerator, depending the 
        # negative/positive signs of the numerator and the denominator
        if self.denominator == 1 or self.denominator == -1:
            result = str(int(self.numerator / self.denominator))
        # If the denominator is the bigger than the numerator, then just return the fraction as it is, depending the negative/positive
        # signs of the numerator and the denominator
        elif abs(self.numerator) < abs(self.denominator):
            if self.numerator > 0 and self.denominator > 0:
                result = f"{self.numerator}/{self.denominator}"
            else:
                result = f"-{abs(self.numerator)}/{abs(self.denominator)}"
        # If the denomintor and numerator is equal, then the fraction is 1 or -1, depending the negative/positive
        # signs of the numerator and the denominator.
        elif abs(self.numerator) == abs(self.denominator):
            if self.numerator > 0 and self.denominator > 0:
                result = "1"
            else:
                result = "-1"
        # Check if the numerator and denominator have the same sign. Note that in the initialization, we already simplify the original
        # fraction, if both the numerator or denominator are negatives.
        # For cases, when both of the numerator or denominator are positives, the fraction is positive
        elif self.numerator > 0 and self.denominator > 0:
            whole_number = self.numerator // self.denominator
            remaining_numerator = self.numerator - whole_number * self.denominator
            remaining_denominator = self.denominator
            remaining_fraction = f"{remaining_numerator}/{remaining_denominator}"
            result = f"{whole_number}+" + remaining_fraction
        # For cases, when only one of the numerator or denominator is negative and the other is positive, the fraction is negative
        else:
            # Need to add one because rounding down negative values is rounding up. For example, -2.73's whole number is -2 not -3
            whole_number = self.numerator // self.denominator + 1
            # Need to take the absolute value, since the remaining fraction needs to be positive because the whole number already has
            # a negative sign in front of it already
            remaining_numerator = abs(self.numerator - whole_number * self.denominator)
            # Need to take the absolute value, since the remaining fraction needs to be positive because the whole number already has
            # a negative sign in front of it already
            remaining_denominator = abs(self.denominator)
            remaining_fraction = f"{remaining_numerator}/{remaining_denominator}"
            result = f"{whole_number}-" + remaining_fraction
        # Returning the result
        return result

    # Creating the as_decimal method to find out the decimal form of the fraction with the precision of 3 decimals
    def as_decimal(self): 
        """Print a fraction object instance as a decimal. Precision to 3 decimal places is sufficient"""
        # Divide the numerator by the denominator with 3 decimal precision and store it as a string  
        result = self.numerator / self.denominator
        string_result = f"{result:.3f}"
        # Returning the result
        return string_result