from rest_framework import generics, permissions
from django.contrib.auth.models import User
from myapp.models import Snippet
from myapp.serializers import SnippetSerializer
from myapp.serializers import UserSerializer
from myapp.permissions import IsOwnerOrReadOnly


# tutorial3 class-based-view
class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # tutorial4 追加 元のcreateメソッドをオーバーライド
    # 作成したスニペットのOwnerにリクエストしたユーザーを登録する。
    def perform_create(self, serializer) -> None:
        serializer.save(owner=self.request.user)


# tutorial3 class-based-view
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    # コードスニペットを作成したユーザーのみに更新・削除権限を与える。
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # tutorial4 追加 元のcreateメソッドをオーバーライド
    # 作成したスニペットのOwnerにリクエストしたユーザーを登録する。
    def perform_create(self, serializer) -> None:
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
