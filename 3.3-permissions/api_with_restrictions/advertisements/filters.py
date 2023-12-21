from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    creator = filters.NumberFilter(field_name="creator_id")
    status = filters.ChoiceFilter(field_name='status', choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['creator', 'title', 'created_at', 'status']
