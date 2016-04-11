from django.shortcuts import render, render_to_response
from forms import UserprofileForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from profiles.models import Userprofile
from .forms import UserprofileForm





def profile(request, profile_id):
    
    if profile_id == "0":
    	if request.user.is_authenticated:
    		userprofile = Userprofile.objects.get(user=request.user)
    else:

    	userprofile = Userprofile.objects.get(pk=profile_id)

    temaplate = 'profiles/profile.html'

    return render(request,temaplate ,{'userprofile':userprofile})



@login_required
def update_profile(request):

    userprofile = Userprofile.objects.get(user=request.user)
    form = UserprofileForm(initial={'bio': userprofile.bio,'picture': userprofile.picture})

    temaplate = 'profiles/update_profile.html'
    return render(request,temaplate,{'form':form})

	
@login_required
def your_profile(request):
	if request.method == 'POST':
		form = UserprofileForm(request.POST, request.FILES or None)
		if form.is_valid():
			userprofile = Userprofile.objects.get(user=request.user)
			bio = form.cleaned_data['bio']
			picture = form.cleaned_data['picture']
			userprofile.bio	= bio 
			userprofile.picture = picture
			userprofile.save()
			return redirect('/profiles/profile/' + str(userprofile.id))
	else:
		form = UserprofileForm()

	return redirect('/profiles/your_profile/')

