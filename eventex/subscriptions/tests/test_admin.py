from unittest.mock import Mock

from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name="Marcos V", cpf="12345678901", phone='47-3333-5555',
                                    email="marcos@marcosvpj.com.br")
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Action mark as paid should be installed"""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """Should mark all selected subscription as paid"""
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """It should send a message to the user"""

        mock = self.call_action()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga')

    def call_action(self):
        queryset = Subscription.objects.all()

        old_message_user = self.model_admin.message_user
        mock = Mock()
        self.model_admin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)
        self.model_admin.message_user = old_message_user

        return mock
