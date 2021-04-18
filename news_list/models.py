from django.db import models
from django.utils import timezone
from django.utils.text import slugify 

class News(models.Model):
    CATEGORIES = [
        ('Sport', 'Sports'),
        ('Technology', 'Technology'),
        ('Culture', 'Culture'),
        ('Other', 'Other')
    ]

    title = models.CharField(max_length=155, default="Title")
    author = models.CharField(max_length=60, default="Author")
    date = models.DateTimeField(default=timezone.now)

    category = models.CharField(
        choices=CATEGORIES,
        default='Other',
        max_length=15
    )

    description = models.TextField(max_length=500, default="Description")
    text = models.TextField(default="Text body")
    thumbnail = models.ImageField(upload_to="images/", default="images/default.png")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


    def __str__(self):
        return self.title