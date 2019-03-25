"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from app01.views.login import LoginView
from app01.views.register import RegView
from app01.views.class_list import ClassList
from app01.views.article_detail import ArticleDetail
from app01.views.today_recommend import TodayRecommend
from app01.views.new_publish import NewPublish
from app01.views.recommend import Recommend
from app01.views.my_article import MyArticle
from app01.views.comment import CommendView
from app01.views.hot_tags import HotTags
from app01.views.article_update import ArticleUpdate
from app01.views.article_add import ArticleAdd
from app01.views.article_delete import ArticleDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegView.as_view()),
    path('today_recommend/', TodayRecommend.as_view()),
    path('new_publish/', NewPublish.as_view()),
    path('class_list/', ClassList.as_view()),
    path('recommend/', Recommend.as_view()),
    path('my_article/', MyArticle.as_view()),
    path('comment/', CommendView.as_view()),
    path('hot_tags/', HotTags.as_view()),
    path('article_update/', ArticleUpdate.as_view()),
    path('article_add/', ArticleAdd.as_view()),
    re_path(r'article_detail/id=(\d+)', ArticleDetail.as_view()),
    re_path(r'article_delete/id=(\d+)', ArticleDelete.as_view()),
]
