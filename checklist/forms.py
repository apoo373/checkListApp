from django.forms import ModelForm
from .models import *

class ItemForm(ModelForm):
    class Meta:
        model = CheckList
        fields = ['title', 'content', 'category', 'priority', 'dateConcerned']
