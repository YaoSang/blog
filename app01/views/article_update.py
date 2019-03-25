# Date: 2019-03-24 下午 10:08

import markdown
from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Article


class ArticleUpdate(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def post(self, request):
        id = request.data['id']
        title = request.data['title']
        markdown = request.data['markdown']
        Article.objects.filter(id=id).update(title=title, content=markdown)

        return Response(self.res.dict)
