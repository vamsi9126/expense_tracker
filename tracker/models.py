from django.db import models

# Create your models here.
class Current_balance(models.Model):
    current_balance = models.FloatField(default=0)
class Tracker(models.Model):
    current_balance = models.ForeignKey(Current_balance, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    expense_type = models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit' )], max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
