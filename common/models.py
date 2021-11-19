from django.db import models


class Group(models.Model):
    pass


class Item(models.Model):
    
    class Type(models.TextChoices):
        THING = ('A', 'Thing')
        OTHER = ('O', 'Other')
    
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    type = models.CharField(max_length = 1, choices = Type.choices, db_index = True)

