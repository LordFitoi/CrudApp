
from django import forms
# from .models import Relationship


class DateInput(forms.DateInput):
    input_type = "date"


# class CreateBudgetSheetForm(forms.Form):
#     name = forms.CharField(max_length=150, required=True)
#     category = forms.ChoiceField(
#         choices=Relationship.choices,
#         required=True)

#     date = forms.DateField(
#         required=True,
#         widget=DateInput())
    
