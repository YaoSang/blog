# Date: 2019-01-10 下午 07:33
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response

from app01.models import UserInfo
from app01.utils.response import BaseResponse

"""
登录
200     OK
201     用户不存在
202     用户名或密码错误

"""


class LoginView(APIView):
    res = BaseResponse()

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = UserInfo.objects.filter(username=username)
            if not user:
                self.res.code = 201
                self.res.msg = "用户不存在"

            else:
                user_obj = auth.authenticate(username=username, password=password)
                if user_obj:
                    self.res.code = 200
                    self.res.data["username"] = username
                else:
                    self.res.code = 202
                    self.res.msg = "用户名或密码错误"
        except Exception as e:
            self.res.msg = str(e)

        return Response(self.res.dict)
