from django.db import models

# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=100, unique=True)
    tag = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20, blank=True)
    add_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-add_time']
        db_table = 'tb_content'

    def __str__(self):
        return self.title