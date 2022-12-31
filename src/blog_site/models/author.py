from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio_data = models.TextField()

    def __str__(self):
        return f"Author: {self.name}"

    class Meta:
        db_table = "blog_author"
