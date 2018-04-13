from __future__ import unicode_literals
from django.db import models

class DocumentRight(models.Model):
    data = models.BinaryField()

    def __str__(self):
        return "{} {}".format(self.id,  self.data)

    def __unicode__(self):
        return "{} {}".format(self.id, self.data)

class DocumentLeft(models.Model):
    data = models.BinaryField()

    def __str__(self):
        return "{} {}".format(self.id,  self.data)

    def __unicode__(self):
        return "{} {}".format(self.id, self.data)

