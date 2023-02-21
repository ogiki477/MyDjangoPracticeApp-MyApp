from django.db import models
from django.utils.timezone import localtime, now
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=localtime(now()).date())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = localtime(now()).date()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('blogApp:post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title




class Comment(models.Model):
    post = models.ForeignKey('blogApp.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=localtime(now()).date())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('blogApp:post_list')

    def __str__(self):
        self.text


