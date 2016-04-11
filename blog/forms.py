from django import forms
from .models import Post

class NameForm(forms.ModelForm):

    
    class Meta:
        model = Post

        #error_css_class = 'error'
        #required_css_class = 'required'
        fields = ('title','content','published',)


class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not extension =="edu":
            raise forms.ValidationError("please use a valid email at eduaction")
        return email

