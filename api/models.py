from django.db import models

# Create your models here.


class Dustbins(models.Model):
    location_name = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.location_name

    # for python 2.x compatibility
    def __unicode__(self):
        return self.location_name


class Readings(models.Model):
    dustbin_id = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    recorded_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    # def __str__(self):
    #     return str(self.level)

    # # for python 2.x compatibility
    # def __unicode__(self):
    #     return str(self.level)

    def __int__(self):
        return int(self.level)
