from django.db import models

# Create your models here.


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        qs = self.get_queryset().filter(
            draft=False
        )
        return qs


class Memes(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name="MEMeTitle", default="title")
    image = models.CharField(max_length=100, blank=False, verbose_name="memePic", default="memePic")
    text1 = models.CharField(max_length=50, blank=False, verbose_name="text1", default="funny")
    text2 = models.CharField(max_length=50, blank=False, verbose_name="text2", default="funny")
    
    objects = PostManager()

    class Meta:
        ordering = ['-id']
