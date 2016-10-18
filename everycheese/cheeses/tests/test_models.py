from test_plus.test import TestCase
from everycheese.cheeses.models import Cheese


class TestCheese(TestCase):

    def test__str__(self):
        cheese = Cheese.objects.create(
            name="Stracchino",
            description="semi-sweet cheese that goes along well with starches",
            firmness=Cheese.FIRMNESS_SEMI_SOFT
        )
        self.assertEqual(cheese.__str__(), 'Stracchino')
