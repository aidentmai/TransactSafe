from django.db import models

# Create your models here.
class Transaction(models.Model):
    cc_num = models.IntegerField()
    merchant = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    long = models.DecimalField(max_digits=10, decimal_places=7)
    transaction_num = models.CharField(max_length=25)
    merch_lat = models.DecimalField(max_digits=10, decimal_places=7)
    merch_long = models.DecimalField(max_digits=10, decimal_places=7)
    is_fraud = models.BooleanField()
    transaction_date = models.DateTimeField()
    transaction_time = models.TimeField()
    amt_ratio = models.DecimalField(max_digits=10, decimal_places=2)
    daily_transaction_count = models.IntegerField()
    user_location_distance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'ID: {self.id} Transaction Amount ${self.amount}'