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
from django.urls import path

from app01.views.login import LoginView
from app01.views.register import RegView
from app01.views.class_list import ClassList
from app01.views.article_detail import ArticleDetail
from app01.views.today_recommend import TodayRecommend
from app01.views.new_publish import NewPublish
from app01.views.recommend import Recommend
from app01.views.comment import CommendView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegView.as_view()),
    path('today_recommend/', TodayRecommend.as_view()),
    path('new_publish/', NewPublish.as_view()),
    path('class_list/', ClassList.as_view()),
    path('article_detail/', ArticleDetail.as_view()),
    path('recommend/', Recommend.as_view()),
    path('comment/', CommendView.as_view()),
]

