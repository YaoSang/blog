# Date: 2019-03-12 上午 11:01

from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse


class IndexShowList(APIView):
    res = BaseResponse()

    def get(self, request):
        self.res.data = [{
            "id": 74,
            "img": "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1126434354,1247589726&fm=58&bpow=600&bpoh=400",
            "name": "Java Object类",
            "inventory": [
                {
                    "food_how": "\u4e24\u4e2a",
                    "food_name": "\u571f\u8c46",
                    "ind": 0
                }, {
                    "food_how": "250g",
                    "food_name": "\u8c46\u89d2",
                    "ind": 1
                }, {
                    "food_how": "100g",
                    "food_name": "\u4e94\u82b1\u8089",
                    "ind": 2
                }, {
                    "food_how": "\u51e0\u74e3",
                    "food_name": "\u5927\u849c",
                    "ind": 3
                }, {
                    "food_how": "\u4e09\u6bb5",
                    "food_name": "\u5927\u8471",
                    "ind": 4
                }, {
                    "food_how": "10\u7c92",
                    "food_name": "\u82b1\u6912",
                    "ind": 5
                }, {
                    "food_how": "\u4e24\u4e2a",
                    "food_name": "\u5e72\u8fa3\u6912",
                    "ind": 6
                }, {
                    "food_how": "\u5c11\u8bb8",
                    "food_name": "\u82b1\u751f\u6cb9",
                    "ind": 7
                }],
            "author": "张小三",
            "collect": 0,
            "like": 0,
            "class_id": 13,
            "time": "2019-02-27",
        }, {
            "id": 72,
            "img": "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20180516\/8e8eaac09b7f310d4a250cd4b261173a.jpg",
            "name": "\u7ea2\u70e7\u8304\u5b50",
            "inventory": [
                {
                    "food_how": "\u4e00\u4e2a",
                    "food_name": "\u5706\u7d2b\u8304\u5b50",
                    "ind": 0
                }, {
                    "food_how": "\u4e24\u4e2a",
                    "food_name": "\u9752\u6912",
                    "ind": 1
                }, {
                    "food_how": "\u4e00\u4e2a",
                    "food_name": "\u897f\u7ea2\u67ff",
                    "ind": 2
                }, {
                    "food_how": "200g",
                    "food_name": "\u4e94\u82b1\u8089",
                    "ind": 3
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u5927\u849c",
                    "ind": 4
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u751f\u59dc",
                    "ind": 5
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u98df\u7528\u6cb9",
                    "ind": 6
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u76d0",
                    "ind": 7
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u9171\u6cb9",
                    "ind": 8
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u9e21\u7cbe",
                    "ind": 9
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u751f\u59dc",
                    "ind": 10
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u9762\u7c89",
                    "ind": 11
                }],
            "author": "李小四",
            "collect": 2,
            "user_like": "312,378",
            "like": 2,
            "class_id": 65,
            "time": "2018-05-16",
        }, {
            "id": 71,
            "img": "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20180515\/aa4b8d5ce526fa4cb9773a7cf2a9dff0.jpg",
            "name": "\u571f\u8c46\u7096\u8c46\u89d2",
            "inventory": [
                {
                    "food_how": "\u4e00\u4e2a",
                    "food_name": "\u571f\u8c46",
                    "ind": 0
                }, {
                    "food_how": "\u4e00\u628a",
                    "food_name": "\u8c46\u89d2",
                    "ind": 1
                }, {
                    "food_how": "250g",
                    "food_name": "\u4e94\u82b1\u8089",
                    "ind": 2
                }, {
                    "food_how": "\u9002\u91cf",
                    "food_name": "\u5e72\u8fa3\u6912",
                    "ind": 3
                }, {
                    "food_how": "\u9002\u91cf",
                    "food_name": "\u82b1\u6912",
                    "ind": 4
                }, {
                    "food_how": "\u9002\u91cf",
                    "food_name": "\u9171\u6cb9",
                    "ind": 5
                }, {
                    "food_how": "\u9002\u91cf",
                    "food_name": "\u767d\u7cd6",
                    "ind": 6
                }, {
                    "food_how": "\u9002\u91cf",
                    "food_name": "\u76d0",
                    "ind": 7
                }, {
                    "food_how": "\u9002\u91cf",
                    "food_name": "\u751f\u59dc",
                    "ind": 8
                }, {
                    "food_how": "\u4e24\u74e3",
                    "food_name": "\u5927\u849c",
                    "ind": 9
                }],
            "author": "王小五",
            "collect": 0,
            "user_like": "251,279",
            "like": 2,
            "class_id": 13,
            "time": "2018-05-15",
        }, {
            "id": 70,
            "img": "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20180422\/44301bc66312d501bbf84f5d8b73f44a.jpg",
            "name": "\u70e4\u6247\u8d1d",
            "inventory": [
                {
                    "food_how": "\u56db\u4e2a",
                    "food_name": "\u6247\u8d1d",
                    "ind": 0
                }, {
                    "food_how": "\u5c11\u8bb8",
                    "food_name": "\u7c89\u4e1d",
                    "ind": 1
                }, {
                    "food_how": "2\u5934",
                    "food_name": "\u849c",
                    "ind": 2
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u5927\u8471",
                    "ind": 3
                }, {
                    "food_how": "\u5c11\u91cf",
                    "food_name": "\u5c0f\u7c73\u8fa3",
                    "ind": 4
                }],
            "author": "赵小六",
            "collect": 1,
            "user_like": "2",
            "like": 1,
            "class_id": 3,
            "time": "2018-04-22",
        },],

        return Response(self.res.dict)
