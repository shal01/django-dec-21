from django import forms
from book.models import Boooks

class BookForm(forms.ModelForm):
    class Meta:
        model=Boooks
        fields="__all__"