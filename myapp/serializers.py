from django.contrib.auth.models import Group, User
from rest_framework import serializers
from myapp.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# tutorial4 追加
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields: list[str] = ["id", "username", "snippets"]


# add tutorial 1 model serializer class
# ModelSerializerは、デフォルトでcreate, updateメソッドを利用可能にしているため、直接記述する必要はなく、簡潔に記述することが可能
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields: list[str] = [
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        ]
