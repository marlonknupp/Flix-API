from rest_framework import generics
from actors.models import Actor


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = None


class ActorRetrieveUpdateDestroyAPIView(generics,RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = None