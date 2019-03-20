# Date: 2019-03-19 下午 08:27
from django.utils.html import strip_tags

import markdown
from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Article


class NewPublish(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def get(self, request):
        new_publish_article_list = []
        new_publish_article = Article.objects.order_by("-create_time")[:7]
        for article in new_publish_article:
            every_article = {"id": "", "title": "", "create_time": "", "excerpt": "", "user": "", "cate_name": ""}
            excerpt = strip_tags(self.md.convert(article.content))[:90]
            every_article["id"] = article.id
            every_article["title"] = article.title
            every_article["create_time"] = article.create_time.strftime("%Y-%m-%d %H:%M:%S")
            every_article["user"] = article.user.username
            every_article["cate_name"] = article.category.cate_name
            every_article["excerpt"] = excerpt
            new_publish_article_list.append(every_article)
        self.res.data = new_publish_article_list

        return Response(self.res.dict)
