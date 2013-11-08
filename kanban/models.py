from django.db import models


class Card(models.Model):
    description = models.TextField()
    list = models.ForeignKey("List", related_name="cards")

    def __unicode__(self):
        return "".join(self.description.splitlines())[:30] + "..."


class List(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
