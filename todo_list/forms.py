from django import forms
from .models import List

#Create a new class that will get the data in the form of List
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
