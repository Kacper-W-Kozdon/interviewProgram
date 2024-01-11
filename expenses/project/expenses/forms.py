
from django import forms
from django.db.models import Count
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):

    from_Date = forms.DateField()
    to_Date = forms.DateField()
    categories = forms.TypedMultipleChoiceField(choices = {object['category_id'] : object['category_name'] for object in Expense.objects.values('category_id').annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        })
        
    class Meta:
        model = Expense
        fields = ('name', )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['from_Date'].required = False
        self.fields['to_Date'].required = False
        self.fields['categories'].required = False
        

        
        
        
