from django.db import models
from accounts.models import Account
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'photo/blog')
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    text = models.TextField()
    #text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null=True)



    def __str__(self):
        return self.title + '|' + str(self.user)
    




# Create your models here.
