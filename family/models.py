from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Family(models.Model):
    Name = models.CharField(max_length=200, verbose_name="نام خانواده")
    Parrent = models.ForeignKey(User, verbose_name="پدر یا مادر خانواده",on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Childrens(models.Model):
    Name = models.CharField(max_length=200, verbose_name="نام فرزند")
    age = models.IntegerField(verbose_name="سن فرزند")
    family = models.ForeignKey(Family, verbose_name="خانواده",on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="امتیاز فرزند")
    level = models.IntegerField(verbose_name="رتبه فرزند")
    user = models.ForeignKey(User, verbose_name="اکانت فرزند",on_delete=models.CASCADE)
    card_number = models.IntegerField(verbose_name="شماره کارت ",unique=True)

    def __str__(self):
        return self.Name
