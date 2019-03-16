from django.contrib import admin
from app01.models import UserInfo
from app01.models import Article
from app01.models import Category
from app01.models import Comment

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
