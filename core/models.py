from django.db import models

# Create your models here.
class Comments(models.Model):
    Comment = models.TextField(max_length=5000)

    def __str__(self):
        return self.Comment

    class Meta:
        verbose_name = "1 - Comment"
        verbose_name_plural = "1 - Comments"

class Comment_Links(models.Model):
    URL = models.CharField(max_length=5000)

    def __str__(self):
        return self.URL

    class Meta:
        verbose_name = "2 - Video link for commenting"
        verbose_name_plural = "2 - Video links for commenting"

class Channels(models.Model):
    URL = models.CharField(max_length=5000)

    def __str__(self):
        return self.URL

    class Meta:
        verbose_name = "3 - Channel Subscription Link"
        verbose_name_plural = "3 - Channel Subscription Links"
