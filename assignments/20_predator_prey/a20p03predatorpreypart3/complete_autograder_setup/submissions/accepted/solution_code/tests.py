"""
Unit tests:

Test case 1 (1. Should create two offsprings):
Points: 1
"""

import unittest

from prey import Prey
from island import Island


class CodingRoomsUnitTests(unittest.TestCase):
    def test_template(self):
        # Arrange
        isle = Island(3)
        Prey.set_breed_time(0)
        prey = Prey(isle)
        isle.register(prey)
        assert str(isle).count("O") == 1
        print("Before breeding:")
        print(isle)

        expected = 3

        # Act
        prey.breed()
        actual = str(isle).count("O")

        # Assert
        print("After breeding:")
        print(isle)
        message = f"\n\nExpected number of prey ({type(expected)}):\n{expected}"
        message += f"\n\nActual number of prey ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()

"""
I/O tests (Use strict whitespace):

Test case 2:
Points: 3

Input:
7

Output:
Enter seed for randomness: O  O  O  O  .  O  .  O  O  .  
O  O  X  .  O  .  X  O  .  .  
X  O  .  .  .  .  O  .  .  O  
.  .  O  O  O  .  O  O  .  O  
.  O  .  .  .  O  O  O  .  X  
O  O  O  .  X  .  .  O  O  O  
O  O  O  X  O  .  O  .  O  O  
X  O  X  .  O  O  O  .  O  X  
O  .  X  .  .  O  .  O  O  O  
.  .  .  .  .  O  O  .  .  O  

O  .  .  X  O  .  O  .  .  .  
O  X  O  .  O  O  .  O  O  .  
O  .  .  O  .  X  .  .  O  .  
O  O  O  .  .  O  .  .  O  .  
O  .  .  O  O  .  O  .  X  O  
O  .  .  X  .  O  O  .  .  .  
X  X  .  .  .  O  .  O  O  O  
.  .  .  .  X  O  .  .  O  O  
O  .  .  .  .  O  O  O  X  O  
.  X  .  .  O  .  .  .  O  O  

.  O  .  .  O  O  .  O  O  .  
X  O  .  O  X  O  O  .  .  .  
.  O  O  O  X  .  .  .  .  O  
.  .  .  .  .  .  .  O  O  O  
O  O  .  X  .  O  O  .  O  .  
X  X  .  .  O  .  .  O  X  O  
.  .  .  .  O  X  O  .  O  .  
.  .  .  .  .  O  O  O  X  .  
.  .  .  .  .  .  .  .  O  .  
X  .  .  O  O  .  O  O  O  .  

O  X  O  .  .  .  O  O  O  O  
O  O  O  O  O  .  O  O  O  O  
.  O  O  X  .  O  O  O  O  O  
.  O  X  X  .  O  .  O  O  O  
X  X  .  .  .  O  .  O  X  O  
.  .  .  O  O  O  O  .  O  O  
.  .  .  .  .  O  O  O  O  O  
.  .  O  O  X  O  O  X  O  .  
.  .  .  O  O  O  O  O  O  O  
.  .  O  .  O  O  O  O  O  .  

O  X  .  O  O  O  O  .  O  .  
O  .  X  X  O  O  O  O  O  O  
O  .  X  X  .  .  O  O  O  O  
O  X  .  .  O  .  O  O  O  X  
.  .  .  .  O  O  O  O  O  .  
.  .  .  X  O  O  O  O  O  O  
.  .  O  O  O  X  O  O  .  O  
.  .  O  O  X  O  X  .  O  O  
.  O  .  O  O  O  O  O  O  .  
.  .  .  O  O  O  O  O  O  O  

.  .  X  O  O  O  O  O  O  O  
X  X  .  O  X  O  O  O  O  O  
O  X  X  O  O  O  O  O  O  O  
.  .  .  .  X  O  O  O  X  X  
.  O  .  O  O  O  O  O  O  O  
.  .  X  O  X  O  O  O  O  O  
.  O  .  O  .  O  O  O  O  O  
.  O  O  O  O  X  O  O  O  O  
.  .  O  O  O  O  O  X  O  O  
.  .  O  .  O  O  O  X  O  O  

.  .  O  O  O  X  O  O  O  O  
.  .  O  X  O  O  O  O  O  O  
X  .  .  X  .  O  O  O  O  O  
X  .  O  O  O  O  O  O  X  O  
O  .  O  O  O  X  O  O  X  O  
.  O  O  X  O  O  O  O  O  O  
O  O  O  O  X  O  O  O  O  O  
O  O  O  O  O  O  X  O  O  O  
O  O  O  O  O  O  X  O  O  O  
.  .  O  O  O  O  X  O  O  O  

.  O  O  X  .  O  O  O  O  O  
.  O  .  X  X  O  O  O  O  O  
.  O  O  O  O  O  O  O  X  O  
X  O  .  .  X  O  O  O  O  O  
.  X  O  O  .  O  O  O  O  X  
O  O  O  X  O  O  X  O  O  .  
O  O  X  O  O  O  O  X  O  O  
O  O  O  O  O  O  O  O  O  O  
O  O  O  O  O  O  O  X  O  O  
.  O  O  O  O  O  .  X  O  O  

O  O  .  .  .  X  O  O  O  O  
O  .  .  .  O  X  O  O  O  X  
O  .  O  O  X  O  O  O  O  .  
.  O  O  O  O  O  O  O  O  O  
X  O  X  O  X  O  O  X  O  O  
O  O  O  O  O  O  X  O  O  X  
O  O  X  O  X  O  O  O  O  O  
O  O  X  O  O  O  O  X  X  O  
O  O  O  O  O  O  O  O  X  O  
O  O  O  O  O  O  O  .  X  O  

.  .  O  O  O  O  O  O  O  .  
.  O  O  O  .  O  X  O  O  O  
O  O  .  O  X  O  O  O  X  O  
O  O  O  .  O  X  O  X  O  .  
O  X  O  X  .  O  X  O  O  O  
O  X  O  O  O  X  .  .  O  O  
O  O  O  X  X  O  O  X  O  X  
O  X  O  O  O  O  O  O  O  O  
O  O  O  O  O  O  X  X  X  O  
O  O  O  O  O  O  O  O  O  X  

O  O  O  O  O  O  O  O  O  O  
O  O  O  O  O  X  O  X  O  O  
O  O  O  X  O  O  X  O  X  O  
O  O  O  O  O  O  O  .  X  O  
X  O  O  O  O  O  O  O  O  O  
X  O  O  X  X  X  X  O  O  X  
O  O  X  X  O  O  X  O  .  X  
O  O  O  O  O  X  O  O  X  O  
O  O  X  O  O  O  O  X  O  O  
O  O  O  O  O  O  X  O  X  O  
"""
