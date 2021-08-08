from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=200)

class Parameter(models.Model):
    app = models.ForeignKey(App, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class ConfigRequest(models.Model):
    app = models.ForeignKey(App, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
