from django.core import mail
from django.test import TestCase


class SubscribePostValidTest(TestCase):
    def setUp(self):
        data = dict(
            name='Marcos Vinicios',
            cpf='12345678901',
            email='marcos@marcosvpj.com.br',
            phone='47-9649-2097'
        )
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'marcos@marcosvpj.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Marcos Vinicios',
            '12345678901',
            'marcos@marcosvpj.com.br',
            '47-9649-2097',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)