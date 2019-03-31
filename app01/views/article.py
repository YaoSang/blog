# Date: 2019-03-20 上午 10:39

import markdown

from rest_framework.views import APIView
from rest_framework.response import Response

from app01.utils.response import BaseResponse
from app01.models import Article
from app01.models import Tag


class ArticleDetail(APIView):
    res = BaseResponse()

    def get(self, request, id):
        article = Article.objects.filter(id=id).first()
        article.total_views += 1
        article.save()
        md = markdown.Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ]
        )
        tag = ""
        data = {
            "id": "",
            "title": "",
            "content": "",
            "create_time": "",
            "modify_time": "",
            "user": "",
            "tags": "",
            "total_views": ""
        }
        tag_query = article.tags.all().values("name")
        for t in tag_query:
            tag += ","
            tag += t["name"]
        tag = tag.strip(",")
        data["id"] = article.id
        data["title"] = article.title
        data["content"] = md.convert(article.content)
        data["create_time"] = article.create_time
        data["modify_time"] = article.modify_time
        data["user"] = article.user.username
        data['tag'] = tag
        data["total_views"] = article.total_views
        self.res.data = data
        return Response(self.res.dict)


class MyArticle(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def post(self, request):

        user_id = request.data["user_id"]
        my_article_list = []
        my_articles = Article.objects.filter(user_id=user_id).order_by('-create_time')
        for article in my_articles:
            every_article = {
                "id": "",
                "title": "",
                "create_time": "",
                "user": "",
                "views": ""
            }
            every_article["id"] = article.pk
            every_article["title"] = article.title
            every_article["user"] = article.user.username
            every_article["views"] = article.total_views
            every_article["create_time"] = article.create_time.strftime("%Y-%m-%d %H:%M:%S")
            my_article_list.append(every_article)
        self.res.data = my_article_list
        return Response(self.res.dict)


class ArticleAdd(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def post(self, request):
        title = request.data['title']
        tag = request.data['tag']
        context = request.data['context']
        try:
            article = Article.objects.create(
                title=title,
                content=context,
                user_id=1,
            )
            tags = Tag.objects.all()
            for t in tags:
                if t.name == tag:
                    break
                else:
                    Tag.objects.create(name=tag)
                    break
            add_tag = Tag.objects.filter(name=tag)
            article.tags.add(add_tag)
            return Response(self.res.dict)

        except Exception as e:
            self.res.data = str(e)
            return Response(self.res.dict)


class ArticleDelete(APIView):
    res = BaseResponse()

    def post(self, request, id):
        Article.objects.filter(id=id).delete()
        return Response(self.res.dict)


class ArticleUpdate(APIView):
    res = BaseResponse()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )

    def post(self, request):
        list = []
        tags = request.data["tag"]
        tag_list = tags.strip("").split(",")  # 前端传过来的标签列表
        for tag in tag_list:
            article = Tag.objects.filter(name=tag).first()
            if not article:
                Tag.objects.create(name=tag)
            else:
                continue
        for j in tag_list:
            tag = Tag.objects.filter(name=j).first()
            list.append(tag)

        id = request.data['id']
        title = request.data['title']
        markdown = request.data['markdown']

        article = Article.objects.filter(id=id).first()
        article.title = title
        article.content = markdown
        article.tags.set(list)
        article.save()
        return Response(self.res.dict)


class ArticleSearch(APIView):
    res = BaseResponse()

    def post(self, request):
        # 先根据标签找出所有的文章,再使用模糊查询找出所有包含关键字的文章
        article_list_obj = []

        search_field = request.data['search']

        if not search_field:
            return
        try:
            tag_obj = Tag.objects.filter(name=search_field).first()
            if not tag_obj:
                article_list = Article.objects.filter(title__contains=search_field)
            else:  # 如果可以通过标签找到对应的文章
                article_list = tag_obj.article_set.all()
            for article in article_list:
                article_obj = dict({"id": "", "title": "", "create_time": "", "user": "", "views": ""})
                article_obj['id'] = article.id
                article_obj['title'] = article.title
                article_obj['user'] = article.user.username
                article_obj['create_time'] = article.create_time.strftime("%Y-%m-%d %H:%M:%S")
                article_obj['views'] = article.total_views
                article_list_obj.append(article_obj)
            self.res.data = article_list_obj

        except Exception as e:
            self.res.code = 201
            self.res.data = str(e)
        return Response(self.res.dict)
