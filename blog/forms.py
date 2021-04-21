from django import forms
from .models import Post,Contribution
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):

    class Meta:

        model =  Post
        fields = '__all__'


class ContributionForm(forms.ModelForm):
    
    class Meta:
        model = Contribution
        fields = ['user','contribution']
