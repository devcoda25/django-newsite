from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "category"

class Post(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='poster')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    links= models.URLField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"



