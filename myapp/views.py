from myapp.models import Snippet
from myapp.serializers import SnippetSerializer
from rest_framework import generics


# tutorial3 class-based-view
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# tutorial3 class-based-view
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
