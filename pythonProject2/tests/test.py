import pytest
from app.calc import Calculator
class TestCalc:
    def setup(self):
        self.calc=Calculator

    def test_subtraction_success(self):
        assert self.calc.subtraction(self,10,2)==8

    def test_multiplication_success(self):
        assert self.calc.multiply(self,10,2)==20

    def test_adding_success(self):
        assert self.calc.adding(self,1,1)==2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self,1,1)==3

    def test_dividingzero_unsuccess(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)

    def teardown(self):
        print("Successful TearDown")
