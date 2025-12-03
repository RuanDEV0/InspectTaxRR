from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True, help_text='Código identificador na API de origem')
    acronym = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.acronym})" if self.acronym else self.name

class Daily(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='daily_units')
    code_api = models.CharField(max_length=50, unique=True)

    recipient_name = models.CharField(max_length=100)
    recipient_cpf = models.CharField(max_length=50, blank=True, null=True)

    date_payment = models.DateField(help_text="Date de referẽncia para o filtro 'Por data'")
    value = models.DecimalField(decimal_places=2, max_digits=12, help_text="Valor total da diaria")

    reason = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Daily"
        verbose_name_plural = "Dailies"
        ordering = ['-date_payment']
        indexes = [
            models.Index(fields=['date_payment']),
            models.Index(fields=['unit']),
        ]

    def __str__(self):
        return f"{self.date_payment} - {self.recipient_name} - {self.value}"