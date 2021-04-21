from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length = 30)
    content = models.TextField()

    def __str__(self):
        return self.title

class Contribution(models.Model):
    
    cat = [('author','Author'),('editor','Editor')]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    contribution = models.CharField(max_length=30,choices=cat)

    class Meta:
        unique_together = (("user", "post","contribution"),)

    def __str__(self):
        return self.contribution
    
