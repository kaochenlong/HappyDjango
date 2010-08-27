from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)
    content = models.TextField()
    publish_data = models.DateField()
    cost = models.IntegerField()
    
    class Meta:
        db_table = "book"