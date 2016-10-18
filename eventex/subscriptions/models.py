from django.db import models

from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):
    name = models.CharField(max_length=100, verbose_name='nome')
    cpf = models.CharField(max_length=11, verbose_name='CPF', validators=[validate_cpf])
    email = models.EmailField(verbose_name='E-mail', blank=True)
    phone = models.CharField(max_length=20, verbose_name='telefone', blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('created_at',)

    def __str__(self):
        return self.name
