# Date: 2019-03-12 下午 03:58
from django.utils.html import strip_tags

import markdown
from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Article


class TodayRecommend(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def get(self, request):
        recommend = []
        today_recommend = Article.objects.all()[0:4]
        for article in today_recommend:
            every_recommend = {"id": "", "title": "", "excerpt": ""}
            excerpt = strip_tags(self.md.convert(article.content))[:30]
            every_recommend["id"] = article.pk
            every_recommend["title"] = article.title
            every_recommend["excerpt"] = excerpt
            recommend.append(every_recommend)
        self.res.data = recommend
        return Response(self.res.dict)
