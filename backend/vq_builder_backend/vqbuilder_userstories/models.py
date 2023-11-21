from django.db import models

# Create your models here.

class queries(models.Model):
    term = models.CharField(max_length = 200)
    score = models.IntegerField()
    rank = models.FloatField()
    week = models.CharField(max_length = 10)
    refresh_date = models.CharField(max_length = 10)

class saved_queries(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    username = models.CharField(max_length = 200)
    query = models.ForeignKey(queries, on_delete = models.CASCADE)

class commentary(models.Model):
    username = models.CharField(max_length = 200)
    comment = models.TextField()
    saved_query = models.ForeignKey(saved_queries, related_name = 'comments', on_delete = models.CASCADE)