from django.forms import ModelForm
from .models import dist1


class dist1_form(ModelForm):

    class Meta:
        model = dist1
        fields = ('title', 'description')
