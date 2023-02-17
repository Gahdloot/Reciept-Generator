from django.db import models

# Create your models here.


#ensure that the last payment id is where the last results is recorded
last_payment_id = 1


class Reciepts(models.Model):
    # add unique
    number = models.IntegerField(default=1)
    amount = models.IntegerField(default=0)
    name_student = models.CharField(max_length=100)
    name_Payer = models.CharField(max_length=100)
    description = models.CharField(max_length=120)
    date_created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.number = self.pk + last_payment_id
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name_student} {self.amount}'