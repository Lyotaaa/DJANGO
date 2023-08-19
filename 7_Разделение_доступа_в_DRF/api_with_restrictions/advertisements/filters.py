from django_filters import rest_framework, DateFromToRangeFilter
from advertisements.models import Advertisement


class AdvertisementFilter(rest_framework.FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ["created_at", "creator", "status"]
