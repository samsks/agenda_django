from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now=True, verbose_name='Registered in')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'events'

    def __str__(self):
        return self.title

    def get_create_date(self):
        return self.event_date.strftime('%d/%m/%Y %H:%Mhrs')
