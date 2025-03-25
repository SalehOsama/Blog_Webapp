from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User                         # we already have a built-in User model Hence, we just need to import it
from django.urls import reverse

class Post(models.Model):                                           # Creating Post model or Table
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)      # creating a relationship between Post and User model.


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})
