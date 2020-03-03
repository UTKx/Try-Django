from django import forms
from myapp.models import Gareeb

class GareebForm(forms.ModelForm):
    
    class Meta:
        model = Gareeb
        # fields = ['name']
        fields = "__all__"