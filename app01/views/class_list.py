# Date: 2019-03-12 下午 03:58

from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Article
from app01.models import Tag


class ClassList(APIView):
    res = BaseResponse()

    def get(self, request):
        data = []
        every_article = dict({"id": "", "title": ""})

        tag_list = Tag.objects.all()
        for tag in tag_list:
            every_tag = dict({"id": "", "name": ""})
            every_tag["id"] = tag.id
            every_tag["name"] = tag.name
            data.append(every_tag)

        self.res.data = [
            {
                "id": 8,
                "class_name": "编程语言",
                "image": None,
                "pid": 0,
                "sort": 1,
                "start": 1,
                "class_names": [
                    {
                        "id": 9,
                        "class_name": "Java",
                        "image": "https://static.easyicon.net/preview/1/13209.gif",
                        "pid": 8,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 10,
                        "class_name": "C++",
                        "image": "https://static.easyicon.net/preview/54/548865.gif",
                        "pid": 8,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 11,
                        "class_name": "PHP",
                        "image": "https://static.easyicon.net/preview/116/1168797.gif",
                        "pid": 8,
                        "sort": 0,
                        "start": 1
                    }
                ]
            }, {
                "id": 15,
                "class_name": "Web前端",
                "image": None,
                "pid": 0,
                "sort": 2,
                "start": 1,
                "class_names": [
                    {
                        "id": 16,
                        "class_name": "Html",
                        "image": "https://static.easyicon.net/preview/116/1168981.gif",
                        "pid": 15,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 17,
                        "class_name": "Css",
                        "image": "https://static.easyicon.net/preview/116/1160494.gif",
                        "pid": 15,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 18,
                        "class_name": "JavaScript",
                        "image": "https://static.easyicon.net/preview/117/1173827.gif",
                        "pid": 15,
                        "sort": 0,
                        "start": 1
                    }
                ]
            }, {
                "id": 58,
                "class_name": "数据库技术",
                "image": "https://static.easyicon.net/preview/122/1225440.gif",
                "pid": 0,
                "sort": 3,
                "start": 1,
                "class_names": [
                    {
                        "id": 59,
                        "class_name": "SQL Server",
                        "image": "https://static.easyicon.net/preview/122/1225435.gif",
                        "pid": 58,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 60,
                        "class_name": "Oracle",
                        "image": "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=4175698249,3336772975&fm=26&gp=0.jpg",
                        "pid": 58,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 61,
                        "class_name": "MySQL",
                        "image": "https://static.easyicon.net/preview/109/1097086.gif",
                        "pid": 58,
                        "sort": 0,
                        "start": 1
                    }
                ]
            }, {
                "id": 1,
                "class_name": "操作系统",
                "image": None,
                "pid": 0,
                "sort": 4,
                "start": 1,
                "class_names": [
                    {
                        "id": 2,
                        "class_name": "Windows",
                        "image": "https://static.easyicon.net/preview/115/1158340.gif",
                        "pid": 1,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 3,
                        "class_name": "Windows Server",
                        "image": "https://static.easyicon.net/preview/123/1230531.gif",
                        "pid": 1,
                        "sort": 3,
                        "start": 1
                    }
                ]
            }, {
                "id": 44,
                "class_name": "软件设计",
                "image": None,
                "pid": 0,
                "sort": 5,
                "start": 1,
                "class_names": [{
                    "id": 45,
                    "class_name": "架构设计",
                    "image": "https://static.easyicon.net/preview/122/1227808.gif",
                    "pid": 44,
                    "sort": 0,
                    "start": 1
                }, {
                    "id": 46,
                    "class_name": "面向对象",
                    "image": "http://img5.imgtn.bdimg.com/it/u=955891249,3286204048&fm=26&gp=0.jpg",
                    "pid": 44,
                    "sort": 0,
                    "start": 1
                },
                ]
            }, {
                "id": 50,
                "class_name": "手机开发",
                "image": None,
                "pid": 0,
                "sort": 6,
                "start": 1,
                "class_names": [
                    {
                        "id": 51,
                        "class_name": "Android开发",
                        "image": "https://static.easyicon.net/preview/118/1188752.gif",
                        "pid": 50,
                        "sort": 0,
                        "start": 1
                    }

                ]
            }, {
                "id": 39,
                "class_name": "企业信息化",
                "image": None,
                "pid": 0,
                "sort": 8,
                "start": 1,
                "class_names": [
                    {
                        "id": 40,
                        "class_name": "BPM",
                        "image": "http://img3.imgtn.bdimg.com/it/u=3106316430,3083687389&fm=26&gp=0.jpg",
                        "pid": 39,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 41,
                        "class_name": "SharePoint",
                        "image": "http://img2.imgtn.bdimg.com/it/u=3077208069,1459002201&fm=26&gp=0.jpg",
                        "pid": 39,
                        "sort": 0,
                        "start": 1
                    }]
            },
            {
                "id": 22,
                "class_name": "其他分类",
                "image": None,
                "pid": 0,
                "sort": 7,
                "start": 1,
                "class_names": [
                    {
                        "id": 23,
                        "class_name": "非技术区",
                        "image": "https://static.easyicon.net/preview/122/1222864.gif",
                        "pid": 22,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 24,
                        "class_name": "软件测试",
                        "image": "http://img2.imgtn.bdimg.com/it/u=1330342731,3196536423&fm=26&gp=0.jpg",
                        "pid": 22,
                        "sort": 0,
                        "start": 1
                    }
                ]
            },
        ]
        return Response(self.res.dict)
