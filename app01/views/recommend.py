# Date: 2019-03-20 上午 10:39
from django.utils.html import strip_tags

import markdown
from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Article


class Recommend(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def get(self, request):
        recommend = []
        recommend_article = Article.objects.order_by('-total_views')[0:5]
        for article in recommend_article:
            every_recommend = {
                "id": "",
                "title": "",
                "user": "",
                "create_time": "",
                "total_views": "",
                "excerpt": "",
            }
            excerpt = strip_tags(self.md.convert(article.content))[:30]
            every_recommend["id"] = article.pk
            every_recommend["title"] = article.title
            every_recommend["user"] = article.user.username
            every_recommend["create_time"] = article.create_time.strftime("%Y-%m-%d %H:%M:%S")
            every_recommend["total_views"] = article.total_views
            every_recommend["excerpt"] = excerpt
            recommend.append(every_recommend)
        self.res.data = recommend
        return Response(self.res.dict)
