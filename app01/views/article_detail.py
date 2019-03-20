# Date: 2019-03-12 上午 11:01

from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse


class ArticleDetail(APIView):
    res = BaseResponse()

    def get(self, request):
        self.res.data = {
                            "id": 1,
                            "name": "\u8292\u679c\u5e03\u4e01",
                            "describe": "\u8fd9\u6b3e\u8292\u679c\u5e03\u4e01\u662f\u7b80\u6613\u7248\u7684\uff0c\u7528\u5e03\u4e01\u7c89\u5236\u4f5c\uff0c\u975e\u5e38\u7b80\u5355\u3002\n\u6211\u7528\u7684\u5e03\u4e01\u7c89\u662f\u7f51\u8d2d\u7684\uff0c\u53f0\u6e7e\u4ea7\u7684\u201c\u597d\u5988\u5988\u201d\uff0c\u5927\u5bb6\u53ef\u4ee5\u5728\u7f51\u4e0a\u641c\u7d22\u4e00\u4e0b\u3002\n\u8fd9\u6b3e\u5e03\u4e01\u7c89\u4e0e\u6c34\u7684\u6bd4\u4f8b\u662f1:6\uff0c\u4e5f\u5c31\u662f100g\u7684\u5e03\u4e01\u7c89+600g\u7684\u6c34\u5236\u6210\u3002\u5efa\u8bae600g\u7684\u6c34\u662f\u7528300g\u7684\u725b\u5976+300g\u7684\u6c34\uff0c\u8fd9\u6837\u7684\u53e3\u611f\u4e0d\u817b\uff0c\u800c\u4e14\u5f88\u5ae9\u6ed1\u3002\n\u6211\u8fd9\u91cc\u7528\u4e86\u4e00\u534a\u7684\u5e03\u4e01\u7c89\u3002\u4e5f\u5c31\u662f50g\u7684\u5e03\u4e01\u7c89+150g\u7684\u6c34+150g\u7684\u725b\u5976\uff0c\u505a\u4e864\u4e2a\u5e03\u4e01\u3002",
                            "author": "\u4f0a\u4eba\u56de\u7738\u6cea\u503e\u57ce ....\u0e08\u0e38\u0e4a\u0e1a",
                            "img": "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/09bca6c9e7ad40dd9e96bc22f89ee7a2.jpg",
                            "class_id": 26,
                            "complexity": "\u4e00\u822c",
                            "handle_time": "10-20\u5206\u949f",
                            "inventory": [{
                                "food_name": "\u8292\u679c\u5e03\u4e01\u7c89",
                                "food_how": "50g"
                            }, {
                                "food_name": "\u725b\u5976",
                                "food_how": "150g"
                            }, {
                                "food_name": "\u6c34",
                                "food_how": "150g"
                            }, {
                                "food_name": "\u5c0f\u8292\u679c",
                                "food_how": "2\u4e2a"
                            }],
                            "step": [
                                "\u8292\u679c\u5207\u6210\u4e01\uff0c\u653e\u5728\u5e03\u4e01\u74f6\u7684\u5e95\u90e8\u3002",
                                "\u5728\u5976\u9505\u91cc\u5012\u5165150g\u7684\u6c34\u548c150g\u7684\u725b\u5976\uff0c\u52a0\u70ed\u81f390\u5ea6\u3002",
                                "\u52a0\u5165\u8292\u679c\u5e03\u4e01\u7c89\u3002",
                                "\u6405\u62cc\u5747\u5300\uff0c\u4f7f\u5e03\u4e01\u7c89\u5b8c\u5168\u6eb6\u89e3\u3002",
                                "\u7528\u6ee4\u7f51\u7b5b\u5165\u5e03\u4e01\u74f6\u4e2d\u3002",
                                "\u51b7\u5374\u81f3\u51dd\u56fa\u5373\u53ef\u98df\u7528\u3002\u653e\u5165\u51b0\u7bb1\u51b7\u85cf\u540e\u98ce\u5473\u66f4\u4f73\u3002"],
                            "thumbnail": [
                                "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/20170915145758280325.jpg",
                                "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/20170915145758467742.jpg",
                                "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/20170915145758118977.jpg",
                                "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/20170915145758925633.jpg",
                                "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/20170915145758592684.jpg",
                                "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/20170915145758258054.jpg"],
                            "tip": "1.\u4e0d\u540c\u54c1\u724c\u7684\u5e03\u4e01\u7c89\u4e0e\u6c34\u7684\u6bd4\u4f8b\u7a0d\u6709\u4e0d\u540c\uff0c\u8bf7\u6839\u636e\u8bf4\u660e\u6765\u5236\u4f5c\u3002\n2.\u653e\u5165\u51b0\u7bb1\u7684\u5e03\u4e01\u8bf7\u57282\u5929\u5185\u5403\u5b8c\u3002",
                            "time": 1505458704,
                            "audit_time": 1505458720,
                            "like": 2,
                            "user_like": "1,2",
                            "click": 108,
                            "collect": 3,
                            "recommend": 0,
                            "status": 1,
                            "uid": 1,
                            "audit_start": 1,
                            "headimgurl": "https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/Q0j4TwGTfTJfTWEjEXibe7sbFXFd2t8CZuM4vKSeS6dFRic4XnyOTRuWibV3vT6IiaV12ZLuP5LEdBhFan0iazupUnQ\/0",
                            "user_like_start": 0,
                            "collect_start": 0
                        },
        return Response(self.res.dict)
