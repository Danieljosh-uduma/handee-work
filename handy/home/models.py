from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    #host =
    head = models.CharField(max_length=100)
    body = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.head[0:50]
    
