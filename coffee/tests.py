from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Coffee

class CoffeeTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_coffee = Coffee.objects.create(
            maker = testuser1,
            name = "Lattee",
            description = "three shots with milk",
        )
        test_coffee.save()

    def test_coffee(self):
        coffee = Coffee.objects.get(id=1)
        actual_maker = str(coffee.maker)
        actual_name = str(coffee.name)
        actual_description = str(coffee.description)
        self.assertEqual(actual_maker, 'testuser1')
        self.assertEqual(actual_name, 'Lattee')
        self.assertEqual(actual_description, 'three shots with milk')