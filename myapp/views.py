from django.contrib.auth.models import Group, User
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from myapp.serializers import GroupSerializer, UserSerializer
from myapp.models import Snippet
from myapp.serializers import SnippetSerializer


# 認証済みのユーザーのみアクセス可能
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes: list = [permissions.IsAuthenticated]


# 認証済みのユーザーのみアクセス可能
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes: list = [permissions.IsAuthenticated]


# tutorial 1 serializer
# tutorial 2 request response
@api_view(["GET", "POST"])
def snippet_list(request, format=None) -> Response | None:
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=200)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# tutorial 2 request response
@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None) -> Response | None:
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=204)
