from django import forms
from myapp1.models import Individual

class IndividualForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    required = True
    error_message="name is required"
    class Meta:
        model=Individual
        # fields=["name","age","description","image"]
        fields=['name','age','description','image','department']
        error = {
            'name':{
                'required':"name is required"
            }
        }

