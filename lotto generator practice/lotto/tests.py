from django.test import TestCase
from lotto.models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected nums')
        g.generate()
        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos) < 20)
