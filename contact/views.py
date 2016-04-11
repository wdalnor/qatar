from django.shortcuts import render
from contact.forms import contactForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def contact(request):

    form = contactForm(request.POST or None)

    title = "Email portal"
    conform_message = None
    if form.is_valid():
    	
        comment = form.cleaned_data['comment']
        send_to = form.cleaned_data['email']
        name = form.cleaned_data['name']
        subject = 'hello my name is : %s' %(name)
        message = '%s' %(comment)
        emailFrom = settings.EMAIL_HOST_USER
        emailTo = [send_to]
        
        send_mail(subject, message, emailFrom, emailTo , fail_silently=True)
        title = "Thanks: "
        conform_message = "we will get back to you soon"
        form = None



    context = {'title': title,'form':form, 'conform_message': conform_message }
    template = 'contact.html'
    return render(request,template, context)
