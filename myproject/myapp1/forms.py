from django import forms
from myapp1.models import Individual

class IndividualForm(forms.ModelForm):
    class Meta:
        model=Individual
        # fields=["name","age","description","image"]
        fields="__all__" # this is to import all
