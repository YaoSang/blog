# Date: 2019-03-20 下午 02:00

from django.utils.html import strip_tags

import markdown
from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from comments.models import Comment


class CommendView(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def get(self, request):
        all_comment = []
        comment_list = Comment.objects.order_by("-created_time")[:3]
        for comment in comment_list:
            every_commend = {
                "id": "",
                "text": "",
                "created_time": "",
                "article": "",
                "excerpt": ""
            }
            excerpt = strip_tags(self.md.convert(comment.text))[:40]
            every_commend["id"] = comment.id
            every_commend["text"] = comment.text
            # every_commend["created_time"] = comment.created_time
            every_commend["article"] = comment.article.title
            every_commend["excerpt"] = excerpt
            all_comment.append(every_commend)
        self.res.data = all_comment
        return Response(self.res.dict)
