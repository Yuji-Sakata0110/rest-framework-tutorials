from django.contrib.auth.models import Group, User
from rest_framework import serializers
from myapp.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# quick start
# HyperlinkedModelSerializer -> モデルインスタンスを特定するためのハイパーリンクを自動生成する。
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields: list[str] = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields: list[str] = ["url", "name"]


# add tutorial 1 model serializer class
# ModelSerializerは、デフォルトでcreate, updateメソッドを利用可能にしているため、直接記述する必要はなく、簡潔に記述することが可能
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields: list[str] = ["id", "title", "code", "linenos", "language", "style"]
