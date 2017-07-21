from unittest.mock import patch
from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class WelcomeTest(TestCase):
    def test_returns_welcome(self):
        response = self.client.get(reverse('welcome:welcome'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, b'Welcome to Grupy-PR!')

class DiceRollTests(TestCase):
    @patch('welcome.views.random')
    def test_rolls_dice_mocked(self, mocked_random):
        response = self.client.get(reverse('welcome:roll_dice'))
        self.assertEquals(response.status_code, 200)
        mocked_random.randint.assert_called_once_with(1, 6)

    def test_rolls_dice(self):
        response = self.client.get(reverse('welcome:roll_dice'))
        self.assertEquals(response.status_code, 200)
        self.assertIn(int(response.content), range(1, 6))
