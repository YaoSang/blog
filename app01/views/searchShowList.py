# Date: 2019-03-12 上午 11:01

from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse


class SearchShowList(APIView):
    res = BaseResponse()

    def get(self, request):
        self.res.data = [{
            "id": 12,
            "img": "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/0140b8a60e012148f9ab5244fdbbf811.jpg",
            "name": "java",
            "inventory": [
                {
                    "food_name": "\u82b9\u83dc\u82d7",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u83b2\u83dc",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u83b4\u7b0b",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u571f\u8c46",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u83dc\u82b1",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u9999\u83dc",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u9999\u83c7",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u8150\u7af9",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u6728\u8033",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u867e",
                    "food_how": "50\u514b"
                }, {
                    "food_name": "\u6cb9",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u76d0",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u767d\u829d\u9ebb",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u9ebb\u8fa3\u9999\u9505\u8c03\u6599",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u8471",
                    "food_how": "10\u514b"
                }, {
                    "food_name": "\u751f\u62bd",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u751f\u59dc",
                    "food_how": "3\u7247"
                }, {
                    "food_name": "\u5927\u849c",
                    "food_how": "\u534a\u5934"
                }],
            "author": "\u4f0a\u4eba\u56de\u7738\u6cea\u503e\u57ce ....\u0e08\u0e38\u0e4a\u0e1a",
            "collect": 1,
            "user_like": "",
            "like": 0,
            "class_id": 64,
            "time": "2017-09-15",
            "nickname": "\u4f0a\u4eba\u56de\u7738\u6cea\u503e\u57ce ....\u0e08\u0e38\u0e4a\u0e1a",
            "headimgurl": "https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/Q0j4TwGTfTJfTWEjEXibe7sbFXFd2t8CZuM4vKSeS6dFRic4XnyOTRuWibV3vT6IiaV12ZLuP5LEdBhFan0iazupUnQ\/0"
        }, {
            "id": 11,
            "img": "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/7a311eaf9f622dfa73bb664186611bf0.jpg",
            "name": "python",
            "inventory": [
                {
                    "food_name": "\u9e21\u7fc5",
                    "food_how": "500\u514b"
                }, {
                    "food_name": "\u571f\u8c46",
                    "food_how": "100\u514b"
                }, {
                    "food_name": "\u76d0",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u7cd6",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u8c46\u74e3\u9171",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u8fa3\u6912",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u6599\u9152",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u8471",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u59dc",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u849c",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u829d\u9ebb",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u82b1\u6912",
                    "food_how": "\u9002\u91cf"
                }],
            "author": "\u4f0a\u4eba\u56de\u7738\u6cea\u503e\u57ce ....\u0e08\u0e38\u0e4a\u0e1a",
            "collect": 1,
            "user_like": None,
            "like": 0,
            "class_id": 64,
            "time": "2017-09-15",
            "nickname": "\u4f0a\u4eba\u56de\u7738\u6cea\u503e\u57ce ....\u0e08\u0e38\u0e4a\u0e1a",
            "headimgurl": "https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/Q0j4TwGTfTJfTWEjEXibe7sbFXFd2t8CZuM4vKSeS6dFRic4XnyOTRuWibV3vT6IiaV12ZLuP5LEdBhFan0iazupUnQ\/0"
        }, {
            "id": 10,
            "img": "https:\/\/h5php.xingyuanauto.com\/FlowProject\/food\/public\/upload\/uploads\/20170915\/7d4c647bc2f4d159356011b0c4f58e3d.jpg",
            "name": "C++",
            "inventory": [
                {
                    "food_name": "\u80e1\u841d\u535c",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u897f\u7ea2\u67ff",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u83b2\u85d5",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u6c34\u53d1\u6728\u8033",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u6c34\u53d1\u9999\u83c7",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u897f\u82b9",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u767d\u841d\u535c",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u9999\u5e72",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u83b4\u7b0b",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u6d0b\u8471",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u9752\u6912",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u87f9\u68d2",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u4e94\u82b1\u8089",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u814a\u80a0",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u5927\u660e\u867e",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u9c7f\u9c7c",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u5e72\u8fa3\u6912",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u671d\u5929\u6912",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u8471",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u59dc",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u76d0",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u8c46\u74e3\u9171",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u6599\u9152",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u767d\u7cd6",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u80e1\u6912\u7c89",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u8fa3\u6912\u6cb9",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u5b5c\u7136\u7c89",
                    "food_how": "\u9002\u91cf"
                }, {
                    "food_name": "\u9ebb\u6cb9",
                    "food_how": "\u9002\u91cf"
                }],
            "author": "S\u2026@\u828a",
            "collect": 1,
            "user_like": None,
            "like": 0,
            "class_id": 64,
            "time": "2017-09-15",
            "nickname": "S\u2026@\u828a",
            "headimgurl": "https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/DYAIOgq83epYNWp8icdXOg10cMX0Ms4s7VKoqbeoKC9XCo9sCFnFuZoqWg5X93zhWnLsDGrdBCjhkSwGkEKuI8g\/0"
        }],
        return Response(self.res.dict)
