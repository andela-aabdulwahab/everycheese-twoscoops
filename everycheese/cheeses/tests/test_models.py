from test_plus.test import TestCase
from .factories import CheeseFactory


class TestCheese(TestCase):

    def test__str__(self):
        cheese = CheeseFactory()
        self.assertEqual(cheese.__str__(), cheese.name)
