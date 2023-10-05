from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel


def car_filtered_queryset(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:

            case 'id_gt':
                qs = qs.filter(id__gt=v)
            case 'id_lt':
                qs = qs.filter(id__lt=v)
            case 'id_gte':
                qs = qs.filter(id__gte=v)
            case 'id_lte':
                qs = qs.filter(id__lte=v)

            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)

            case 'seats_gt':
                qs = qs.filter(seats__gt=v)
            case 'seats_lt':
                qs = qs.filter(seats__lt=v)
            case 'seats_gte':
                qs = qs.filter(seats__gte=v)
            case 'seats_lte':
                qs = qs.filter(seats__lte=v)

            case 'engine_v_gt':
                qs = qs.filter(engine_v__gt=v)
            case 'engine_v_lt':
                qs = qs.filter(engine_v__lt=v)
            case 'engine_v_gte':
                qs = qs.filter(engine_v__gte=v)
            case 'engine_v_lte':
                qs = qs.filter(engine_v__lte=v)

            case 'model_startswith':
                qs = qs.filter(model__startswith=v)
            case 'model_contains':
                qs = qs.filter(model__contains=v)
            case 'model__endswith':
                qs = qs.filter(model__endswith=v)

            case 'type_startswith':
                qs = qs.filter(type__startswith=v)
            case 'type_contains':
                qs = qs.filter(type__contains=v)
            case 'type__endswith':
                qs = qs.filter(type__endswith=v)

            case 'order_by':
                qs = qs.order_by(v)

            case _:
                raise ValidationError({'detail': f'{k} is not allowed here'})

    return qs
