from django import forms 
from django.contrib.auth.models import User
from rango.models import Category, Page
from rango import fofo

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Add New Category.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    


    class Meta:
        model = Category
        fields= ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    url = forms.URLField(max_length=200)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:

        model = Page
        exclude = ('category',)



'''
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # if url is not empty and doesnot start with http//, prepend 'http://'.
        if url and not url.startswith('http://'):

            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data
'''

class UserForm(forms.ModelForm):


    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:

        model = User
        fields = ('username', 'email', 'password')














