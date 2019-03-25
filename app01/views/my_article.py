# Date: 2019-03-20 上午 10:39
from django.utils.html import strip_tags

import markdown
from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Article


class MyArticle(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def get(self, request):
        my_article_list = []
        my_articles = Article.objects.order_by('-create_time')
        for article in my_articles:
            every_article = {
                "id": "",
                "title": "",
                "create_time": "",
                "user": "",
                "views": ""
            }
            every_article["id"] = article.pk
            every_article["title"] = article.title
            every_article["user"] = article.user.username
            every_article["views"] = article.total_views
            every_article["create_time"] = article.create_time.strftime("%Y-%m-%d %H:%M:%S")
            my_article_list.append(every_article)
        self.res.data = my_article_list
        return Response(self.res.dict)
