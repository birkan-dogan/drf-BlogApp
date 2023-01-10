from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name


class Blog(models.Model):

    category = models.ForeignKey(Category, on_delete = models.PROTECT)  # category_id
    title = models.CharField(max_length = 100, unique = True)
    content = models.TextField(blank = True)
    is_published = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
