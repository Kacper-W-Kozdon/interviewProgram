from collections import OrderedDict
from django.db.models import DateTimeField
from datetime import datetime
from django.db.models import Sum, Value, Count
from django.db.models.functions import Coalesce
from django.db.models.functions import (
     ExtractDay,
     ExtractMonth,
     ExtractQuarter,
     ExtractWeek,
     ExtractWeekDay,
     ExtractIsoYear,
     ExtractYear,
 )


def summary_per_category(queryset):
    ret = OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))
    Total = sum([total for _, total in ret.items()])
    return ret, Total

def summary_per_month(queryset):
    return tuple(sorted(
        queryset
        .annotate(year=ExtractYear('date'), month=ExtractMonth('date'))
        .order_by()
        .values('year', 'month')
        .annotate(s=Sum('amount'))
        .values_list('year', 'month', 's')))

def quantity_per_category(queryset):
    return OrderedDict(
        queryset
        .values('category__name')
        .annotate(s=Count('category'))
        .values_list('category__name', 's')
        .exclude(s__iexact=None)
    )