from django.db import models
from django.urls import reverse

# Create your models here.
# 글의 분류(일상, 유머, 정보)


class Category(models.Model):
    name = models.CharField(
        max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex: 일상)")

    def __str__(self):
        return self.name

# 블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)


class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요. ")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single", args=[str(self.id)])
