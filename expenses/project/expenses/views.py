from django.views.generic.list import ListView
from django.core.paginator import Paginator
from .forms import ExpenseSearchForm
from .models import Expense, Category, Monthly
from .reports import summary_per_category, summary_per_month, quantity_per_category
import json


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5
   
    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        
        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            from_Date = form.cleaned_data.get('from_Date', None)
            to_Date = form.cleaned_data.get('to_Date', None)
            categories = form.cleaned_data.get('categories', None)
            if name:
                queryset = queryset.filter(name__icontains=name)
            if from_Date:
                queryset = queryset.filter(date__range=[from_Date, queryset.order_by('date').last().date])
            if to_Date:
                queryset = queryset.filter(date__range=[queryset.order_by('date').first().date, to_Date])
            if categories:        
                queryset = queryset.filter(category_id__in=categories)
            if 'ordering' in self.request.GET:
                queryset = queryset.order_by(self.request.GET['ordering'], '-id')            
        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset)[0],
            Total=summary_per_category(queryset)[1],
            summary_per_month=summary_per_month(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = Expense.objects.all()
        object_list = self.object_list
        return super().get_context_data(
            object_list=object_list,
            quantity_per_category=quantity_per_category(queryset),
            **kwargs
        )
