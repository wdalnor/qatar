
from django.views import generic 
from .models import Post
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm, ContactForm

class PublishedPostMixin(object):
    def get_queryset(self):
        queryset = super(PublishedPostMixin, self).get_queryset()
        return queryset.filter(published=True)

class PostListView(PublishedPostMixin, generic.ListView):

    model = Post



class PostDetailView(generic.DetailView):

    model = Post
    

def myname(request):

    if request.method == "POST":
        
        form = NameForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return HttpResponseRedirect('/blog/your-name')
    else:

        form = NameForm()

    return render(request, 'blog/name.html', {'form': form})



def contact_form(request):

    form = ContactForm(request.POST)
    if request.method == "POST":
        

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['someMail@example.com']
            if cc_myself:
            
                recipients.append(email)

            send_mail(subject, message, email, recipients)
            return HttpResponseRedirect('/blog/')

    return render(request, 'blog/contact.html', {'form': form})








        
