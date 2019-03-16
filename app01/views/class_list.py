# Date: 2019-03-12 下午 03:58

from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse


class ClassList(APIView):
    res = BaseResponse()

    def get(self, request):
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
                    }, {
                        "id": 12,
                        "class_name": "Python",
                        "image": "https://static.easyicon.net/preview/109/1097222.gif",
                        "pid": 8,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 13,
                        "class_name": "C#",
                        "image": "https://static.easyicon.net/preview/111/1116255.gif",
                        "pid": 8,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 14,
                        "class_name": "c语言",
                        "image": "https://static.easyicon.net/preview/111/1116172.gif",
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
                    }, {
                        "id": 19,
                        "class_name": "JQuery",
                        "image": "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=821957021,1449380298&fm=26&gp=0.jpg",
                        "pid": 15,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 20,
                        "class_name": "Html5",
                        "image": "https://static.easyicon.net/preview/52/522194.gif",
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
                    }, {
                        "id": 62,
                        "class_name": "NoSQL",
                        "image": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2766114427,355645987&fm=27&gp=0.jpg",
                        "pid": 58,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 63,
                        "class_name": "大数据",
                        "image": "https://static.easyicon.net/preview/122/1225435.gif",
                        "pid": 58,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 64,
                        "class_name": "其他数据库",
                        "image": "https://static.easyicon.net/preview/122/1222585.gif",
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
                    }, {
                        "id": 4,
                        "class_name": "Linux",
                        "image": "https://static.easyicon.net/preview/121/1210908.gif",
                        "pid": 1,
                        "sort": 1,
                        "start": 1
                    }, {
                        "id": 5,
                        "class_name": "OS X",
                        "image": "https://static.easyicon.net/preview/118/1188753.gif",
                        "pid": 1,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 6,
                        "class_name": "嵌入式",
                        "image": "https://static.easyicon.net/preview/119/1199088.gif",
                        "pid": 1,
                        "sort": 0,
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
                }, {
                    "id": 47,
                    "class_name": "设计模式",
                    "image": "https://static.easyicon.net/preview/123/1232071.gif",
                    "pid": 44,
                    "sort": 0,
                    "start": 1
                }, {
                    "id": 48,
                    "class_name": "领域驱动设计",
                    "image": "https://static.easyicon.net/preview/121/1218052.gif",
                    "pid": 44,
                    "sort": 0,
                    "start": 1
                }
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
                    }, {
                        "id": 52,
                        "class_name": "iOS开发",
                        "image": "https://static.easyicon.net/preview/121/1212959.gif",
                        "pid": 50,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 54,
                        "class_name": "Windows Phone",
                        "image": "https://static.easyicon.net/preview/121/1210167.gif",
                        "pid": 50,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 55,
                        "class_name": "Windows Mobile",
                        "image": "https://static.easyicon.net/preview/122/1227836.gif",
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
                    }, {
                        "id": 42,
                        "class_name": "GIS技术",
                        "image": "https://static.easyicon.net/preview/116/1168978.gif",
                        "pid": 39,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 53,
                        "class_name": "企业信息化其他",
                        "image": "https://static.easyicon.net/preview/123/1232062.gif",
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
                    }, {
                        "id": 25,
                        "class_name": "代码与软件发布",
                        "image": "https://static.easyicon.net/preview/122/1227806.gif",
                        "pid": 22,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 26,
                        "class_name": "计算机图形学",
                        "image": "https://static.easyicon.net/preview/122/1229312.gif",
                        "pid": 22,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 27,
                        "class_name": "游戏开发",
                        "image": "https://static.easyicon.net/preview/121/1215322.gif",
                        "pid": 22,
                        "sort": 0,
                        "start": 1
                    }, {
                        "id": 28,
                        "class_name": "程序人生",
                        "image": "https://static.easyicon.net/preview/122/1227804.gif",
                        "pid": 22,
                        "sort": 0,
                        "start": 1
                    }
                ]
            },
        ]
        return Response(self.res.dict)
