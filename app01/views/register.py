# Date: 2019-01-17 下午 09:12


from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import UserInfo

"""
注册
200     OK
201     用户已存在
202     注册错误

"""


class RegView(APIView):
    res = BaseResponse()

    def post(self, request):
        try:
            reg_username = request.data.get("reg_username")
            reg_password = request.data.get("reg_password")
            reg_email = request.data.get("reg_email")
            user = UserInfo.objects.filter(username=reg_username)
            if user:
                self.res.code = 201
                return Response(self.res.dict)
            user = UserInfo.objects.create_user(username=reg_username, password=reg_password, email=reg_email)
            if user:
                self.res.code = 200
            else:
                self.res.code = 202
        except Exception as e:
            self.res.code = 203
            self.res.msg = str(e)
        return Response(self.res.dict)
