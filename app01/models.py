
from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.


# 用户表
class UserInfo(AbstractUser):
    username = models.CharField(max_length=11, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=128, verbose_name="密码")
    email = models.CharField(max_length=128, verbose_name="邮箱", null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.username


# 标题表
class Category(models.Model):
    cate_name = models.CharField(max_length=32, verbose_name="分类名称")
    pid = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.cate_name


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=32, verbose_name="文章标题")
    description = models.CharField(max_length=32, verbose_name="文章描述", null=True, blank=True)
    content = models.TextField(verbose_name="文章内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    user = models.ForeignKey(UserInfo, verbose_name="用户", on_delete=models.CASCADE)
    cate_name = models.ForeignKey(Category, verbose_name="文章分类", on_delete=models.CASCADE)
    image_name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.title


# 评论表
class Comment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    user = models.ForeignKey(UserInfo, verbose_name="用户", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name="文章", on_delete=models.CASCADE)
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name="父级评论", on_delete=models.CASCADE)

    def __str__(self):
        return self.content
