from django.contrib.auth.models import Group, User
from rest_framework import serializers


# HyperlinkedModelSerializer -> モデルインスタンスを特定するためのハイパーリンクを自動生成する。
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields: list[str] = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields: list[str] = ["url", "name"]
