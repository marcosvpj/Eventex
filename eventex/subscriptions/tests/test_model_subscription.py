from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Marcos Vinicios Pagelkopf Junior',
            cpf='12345678901',
            email='marcos@marcosvpj.com.br',
            phone='47-9649-2097'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscriptio must have an auto created_at attribute"""
        self.assertIsInstance(self.obj.created_at, datetime)
