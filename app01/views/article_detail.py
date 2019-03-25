# Date: 2019-03-12 上午 11:01

from rest_framework.views import APIView
from rest_framework.response import Response

import markdown
from app01.utils.response import BaseResponse
from app01.models import Article


class ArticleDetail(APIView):
    res = BaseResponse()

    def get(self, request, id):
        article = Article.objects.filter(id=id).first()
        md = markdown.Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
        data = {
            "id":"",
            "title":"",
            "content":"",
            "create_time":"",
            "modify_time":"",
            "user":"",
            "category":"",
            "tags":"",
            "total_views":""
        }
        data["id"] = article.id
        data["title"] = article.title
        data["content"] = md.convert(article.content)
        data["create_time"] = article.create_time
        data["modify_time"] = article.modify_time
        data["user"] = article.user.username
        data["category"] = article.category.cate_name
        data["tags"] = article.tags.name
        data["total_views"] = article.total_views
        print(md.convert(article.content))

        self.res.data = data
        return Response(self.res.dict)
