from advertisements.permissions import IsNotDraftOrIsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in [
            "update",
            "partial_update",
            "destroy",
            "remove_from_favorites",
            "add_to_favoritea",
            "favorites",
        ]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        if self.action == "retrieve":
            return [IsNotDraftOrIsOwner()]
        return []

    def list(self, request):
        pass
