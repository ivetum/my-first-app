from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    transaction_date = models.DateField(null=True, blank=True)
    amount = models.FloatField(default=0.0)
    transaction_type = models.ForeignKey('TransactionType')
    entity = models.ForeignKey('Entity')
    project = models.ForeignKey('Project')
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    venue = models.CharField(max_length=200)
    project = models.ForeignKey('Project')
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey('ProjectGroup')
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class ProjectGroup(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Entity(models.Model):
    name = models.CharField(max_length=200)
    identification_number = models.IntegerField(null=True, blank=True)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class TransactionType(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
