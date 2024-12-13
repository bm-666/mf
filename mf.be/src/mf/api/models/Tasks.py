from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)


class PartnerTask(Task):
    name = models.CharField(max_length=100)
    url = models.URLField()
    reward = models.IntegerField()





