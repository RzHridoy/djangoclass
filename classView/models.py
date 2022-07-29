from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.


class Data(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    address = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Payment(models.Model):
    employee = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='payment')
    amount = models.FloatField()
    choice = (
        (0, 'Done'),
        (1, 'Pending')
    )
    status = models.IntegerField(choices=choice)

    def __str__(self):
        return str(self.amount) + ' ' + str(self.status)

    def get_absolute_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.pk})
