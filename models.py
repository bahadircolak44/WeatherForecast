from django.db import models


class TurkeyCities(models.Model):
    city_name = models.CharField(max_length=50, null=False)
