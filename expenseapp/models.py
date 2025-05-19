from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRAVEL', 'Travel'),
        ('UTIL', 'Utilities'),
        ('ENT', 'Entertainment'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=100 , default="Untitled")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='OTHER')
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"

