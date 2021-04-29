from django.db import models

from django.core.validators import MinLengthValidator

# An articles model, outlining the possible fields for the article form


class Articles(models.Model):

    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=200, unique=True)
    article_image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    intro = models.TextField(
        validators=[MinLengthValidator(100)], max_length=400)
    article_content = models.TextField(
        validators=[MinLengthValidator(250)], null=True, blank=True)

    def __str__(self):
        return self.title
