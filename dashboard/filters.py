from datetime import date
import django_filters
from shopping.models import *
from django_filters import DateFilter

class orderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ['customer', 'complete', 'transaction_id', 'date_ordered']