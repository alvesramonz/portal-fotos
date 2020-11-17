from django.forms import ModelForm

from django import forms
from django.contrib.auth.models import User

from visitor.models import Media

class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = ['img']

class MediaUpdateForm(ModelForm):
    class Meta:
        model = Media
        fields = '__all__'