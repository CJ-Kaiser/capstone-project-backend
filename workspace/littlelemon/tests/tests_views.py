from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=200, inventory=10)

    def test_getall(self):
         all = list(Menu.objects.all())
         self.assertEqual(str(all[0]), "IceCream : 80.00")
         self.assertEqual(str(all[1]), "Cake : 200.00")