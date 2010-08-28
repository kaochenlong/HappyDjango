from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)
    content = models.TextField()
    publish_data = models.DateField()
    cost = models.IntegerField()
    
    def __unicode__(self):
        return self.author + ' - ' + self.title
    
    class Meta:
        db_table = "book"