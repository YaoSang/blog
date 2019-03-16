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
from app01.views.FoodInfoData import FoodInfoData
from app01.views.recommend import Recommend
from app01.views.searchShowList import SearchShowList
from app01.views.index_show_list import IndexShowList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegView.as_view()),
    path('recommend/', Recommend.as_view()),
    path('class_list/', ClassList.as_view()),
    path('index_show_list/', IndexShowList.as_view()),
    path('search_show_list/', SearchShowList.as_view()),
    path('food_info_data/', FoodInfoData.as_view()),


]

