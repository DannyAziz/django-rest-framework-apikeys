from rest_framework import generics, mixins

from .models import APIKey
from .serializers import APIKeySerializer


class APIKeyList(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = APIKeySerializer

    def get_queryset(self):
        user = self.request.user
        return APIKey.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class APIKeyCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = APIKeySerializer
    queryset = APIKey.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class APIKeyDelete(mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = APIKeySerializer
    queryset = APIKey.objects.all()
    lookup_url_kwarg = "id"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)