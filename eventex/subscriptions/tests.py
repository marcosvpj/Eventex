from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricoes/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"', 1)
        self.assertContains(self.resp, 'type="submit"', 1)

    def test_csrf(self):
        """Html must contains csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Marcos Vinicios',
            cpf='12345678901',
            email='marcos@marcosvpj.com.br',
            phone='47-9649-2097'
        )
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""

        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

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
        self.assertIn('Marcos Vinicios', self.email.body)
        self.assertIn('12345678901', self.email.body)
        self.assertIn('marcos@marcosvpj.com.br', self.email.body)
        self.assertIn('47-9649-2097', self.email.body)
