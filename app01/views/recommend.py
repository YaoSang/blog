# Date: 2019-03-12 下午 03:58

from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse


class Recommend(APIView):
    res = BaseResponse()

    def get(self, request):
        self.res.data = {
            "code": 1001,
            "data": [
                {
                    "id": 15,
                    "img": "https://ss3.baidu.com/-rVXeDTa2gU2pMbgoY3K/it/u=1802306161,1810111121&fm=202&mola=new&crop=v1",
                    "name": "Java开发面试题汇总",
                    "inventory": [{
                        "food_name": "排骨",
                        "food_how": "400克"
                    }, {
                        "food_name": "冬瓜",
                        "food_how": "500克"
                    }, {
                        "food_name": "油",
                        "food_how": "适量"
                    }, {
                        "food_name": "盐",
                        "food_how": "适量"
                    }, {
                        "food_name": "葱",
                        "food_how": "适量"
                    }, {
                        "food_name": "大料",
                        "food_how": "2个"
                    }, {
                        "food_name": "料酒",
                        "food_how": "15毫升"
                    }, {
                        "food_name": "胡椒粉",
                        "food_how": "适量"
                    }, {
                        "food_name": "鸡精",
                        "food_how": "适量"
                    }, {
                        "food_name": "姜",
                        "food_how": "适量"
                    }],
                    "author": "S…@芊",
                    "collect": 0,
                    "like": 0,
                    "user_like": 1,
                    "time": "2017-09-15"
                },
                {
                    "id": 33,
                    "img": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3758173109,3108079170&fm=26&gp=0.jpg",
                    "name": "Vue组件通讯黑科技",
                    "inventory": [{
                        "food_name": "牛肉",
                        "food_how": "400克"
                    }, {
                        "food_name": "芹菜",
                        "food_how": "800克"
                    }, {
                        "food_name": "饺子皮",
                        "food_how": "1000克"
                    }, {
                        "food_name": "葱花",
                        "food_how": "适量"
                    }, {
                        "food_name": "盐",
                        "food_how": "适量"
                    }, {
                        "food_name": "五香粉",
                        "food_how": "3克"
                    }, {
                        "food_name": "胡椒粉",
                        "food_how": "3克"
                    }, {
                        "food_name": "姜粉",
                        "food_how": "3克"
                    }, {
                        "food_name": "酱油",
                        "food_how": "25毫升"
                    }, {
                        "food_name": "料酒",
                        "food_how": "20毫升"
                    }, {
                        "food_name": "白糖",
                        "food_how": "2克"
                    }, {
                        "food_name": "鸡精",
                        "food_how": "适量"
                    }, {
                        "food_name": "香油",
                        "food_how": "适量"
                    }],
                    "author": "伊人回眸泪倾城 ....จุ๊บ",
                    "collect": 1,
                    "like": 0,
                    "user_like": 1,
                    "time": "2017-09-15"
                },
                {
                    "id": 7,
                    "img": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1552467651939&di=8015067d7114cae73a1965a20cf51ee8&imgtype=0&src=http%3A%2F%2Fimg.mukewang.com%2F5b5146860001e96e19201080.jpg",
                    "name": "Linux系统使用",
                    "inventory": [{
                        "food_name": "冬瓜",
                        "food_how": "400克"
                    }, {
                        "food_name": "猪肉泥",
                        "food_how": "150克"
                    }, {
                        "food_name": "姜",
                        "food_how": "适量"
                    }, {
                        "food_name": "葱",
                        "food_how": "适量"
                    }, {
                        "food_name": "盐",
                        "food_how": "少许"
                    }, {
                        "food_name": "料酒",
                        "food_how": "适量"
                    }, {
                        "food_name": "芝麻油",
                        "food_how": "适量"
                    }, {
                        "food_name": "生粉",
                        "food_how": "少许"
                    }, {
                        "food_name": "胡椒粉",
                        "food_how": "少许"
                    }],
                    "author": "伊人回眸泪倾城 ....จุ๊บ",
                    "collect": 0,
                    "like": 0,
                    "user_like": 1,
                    "time": "2017-09-15"
                },
                {
                    "id": 30,
                    "img": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2266409816,3873172073&fm=26&gp=0.jpg",
                    "name": "Android开发笔记",
                    "inventory": [{
                        "food_name": "大包粉",
                        "food_how": "500克"
                    }, {
                        "food_name": "糖",
                        "food_how": "75克"
                    }, {
                        "food_name": "酵母",
                        "food_how": "4克"
                    }, {
                        "food_name": "水",
                        "food_how": "180克"
                    }, {
                        "food_name": "油",
                        "food_how": "20克"
                    }, {
                        "food_name": "流沙馅",
                        "food_how": "250克"
                    }, {
                        "food_name": "猪油",
                        "food_how": "50克"
                    }, {
                        "food_name": "水",
                        "food_how": "75克"
                    }],
                    "author": "伊人回眸泪倾城 ....จุ๊บ",
                    "collect": 1,
                    "like": 2,
                    "user_like": 2,
                    "time": "2017-09-15"
                }
            ],
            "msg": "Query Data Success"
        }

        return Response(self.res.dict)
