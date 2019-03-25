# Date: 2019-03-24 下午 10:49


import markdown
from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Article


class ArticleAdd(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def post(self, request):
        title = request.data['title']
        context = request.data['context']
        print(context)
        article = Article.objects.create(title=title, content=context, user_id=1, category_id=1)
        if article:
            return Response(self.res.dict)
        else:
            return Response(self.res.dict)
