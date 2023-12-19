from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    creator = filters.NumberFilter(field_name="creator_id")

    class Meta:
        model = Advertisement
        fields = ['creator', 'title', 'created_at']
