from django.db import models

# Create your models here.


# modelo de post 
class Posts(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='image/')
    cretae_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
