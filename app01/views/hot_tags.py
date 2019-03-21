# Date: 2019-03-20 下午 08:41

from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Tag


class HotTags(APIView):
    res = BaseResponse()

    def get(self, request):
        tag_list = []
        tags = Tag.objects.all()

        for tag in tags:
            every_tag = {"id": "", "title": ""}
            every_tag["id"] = tag.id
            every_tag["title"] = tag.name
            tag_list.append(every_tag)
        self.res.data = tag_list

        return Response(self.res.dict)
