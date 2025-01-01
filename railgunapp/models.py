from django.db import models
from django.contrib.auth.models import User

class Category1(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True)
    slug = models.SlugField()
    body = models.TextField()
    background = models.CharField(max_length=1000, null=True)
    image = models.CharField(max_length=1000, null=True)
    slogan = models.CharField(max_length=200, null=True)
    first_category = models.ForeignKey(Category1, on_delete=models.CASCADE)
    second_category = models.ForeignKey(Category2, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    number_of_clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Settings(models.Model):
    module = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    qno = models.IntegerField(default=0)

    def __str__(self):
        return self.module + ";" + self.topic + ";" + str(self.qno)
    
class Answer(models.Model):
    question = models.CharField(max_length=1000, null=True)
    answer = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.question[:100]