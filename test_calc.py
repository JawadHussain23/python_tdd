import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        calculator = Calc()                 #Arrange
        result = calculator.add(10,2)       #Act
        self.assertEqual(result, 12)        #Assert
    
    def test_sub(self):
        calculator = Calc()                 #Arrange
        result = calculator.sub(10,2)       #Act
        self.assertEqual(result, 8)         #Assert
    
    def test_multiply(self):
        calculator = Calc()                  #Arrange
        result = calculator.multiply(10,2)   #Act
        self.assertEqual(result, 20)         #Assert
    
    def test_division(self):
        calculator = Calc()                 #Arrange
        result = calculator.division(10,2)  #Act
        self.assertEqual(result, 5)         #Assert
        