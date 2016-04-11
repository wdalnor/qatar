
from django.shortcuts import render
from rango.forms import CategoryForm, PageForm, UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Category, Page
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from rango.bing_search import run_query
from django.shortcuts import redirect


def home(request):

    '''request.session.set_test_cookie()'''
    category_list = Category.objects.order_by('-likes')[:50]
    #page_list = Page.objects.order_by('views')[:5]
    roro = " I will never give up and I will do my best to be successful person"
 #   context = {"categories":category_list,'pages': page_list}

    context = {"categories":category_list}
#   get the number of visits to the site.
#  we use the cookie.get() function to obtain the visits cookies
#  if the cookie exists, the value returned is casted to an integer .
#if the cookie does not exits, we default to zero and cast that

    visits = request.session.get('visits')
    if not visits:
        visits = 1

    reset_last_visit_time = False
    
     
    last_visit = request.session.get('last_visit')
    # does the cookie last_vist exits ?
    if last_visit:
        
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
         # if it is been more than a day since last visit ...
        if (datetime.now() - last_visit_time).seconds > 0:

            visits = visits + 1
    # and falge that the cookie last visit needs to be updated 

            reset_last_visit_time = True

    else:

        reset_last_visit_time = True

    if reset_last_visit_time:

        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context['visits'] = visits

    return render(request, 'rango/index.html', context)




    #return response


def about(request):

    fo = "some people are great "
    context = {"gott": fo }
    return render(request,'rango/about.html', context)


def category(request, category_name_slug):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

            context_dict['result_list'] = result_list
            context_dict['query'] = query

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category).order_by('-views')
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    if not context_dict['query']:
        context_dict['query'] = category.name

    return render(request, 'rango/category.html', context_dict)



def add_category(request):

    if request.method == 'POST':

        form = CategoryForm(request.POST)
        if form.is_valid():

            form.save(commit=True)
            return home(request)

        else:
            print form.errors

    else:

        form = CategoryForm()


    return render(request, 'rango/add_category.html', {'form': form})


def Display_Meta(request):

    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))




def add_page(request, category_name_slug):



    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.save()
                # probably better t use a redirect here
                return HttpResponseRedirect('/rango/')
                #old way >>> (return category(request, category_name_slug))


        else:
            print form.errors

    else:

        form = PageForm()


    context_dict = {'form': form, 'category': cat}
    return render(request, 'rango/add_page.html', context_dict)



def register(request):

    # a boolean value telling the template that the registration was successful
   # set to false initailly. code changes value to true whenregistration succeeds . 

    #if request.session.test_cookie_worked():
      #  print " >>>> TEST COOKIE WORKED "
        

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

        # Now we hash the password with the set_password method . 
        # once hashed  we can update the user object

            user.set_password(user.password)

            user.save()

            # Now sort out the userprofile instance
            # once hashed , we can update the user object

            # this delay saving the model until we are ready to avoid integrity problems.


           
           
            #did the user provides a profile picture?
           #if so , we need to set the user attribute ourselves, we set commit =False.
         
           

            return HttpResponseRedirect('/rango/')


            registered = True

        else:
            print user_form.errors


    else:
        user_form = UserForm()
       

    return render(request, 'rango/register.html', {'user_form': user_form,'registered': registered })
   


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled call mr Mohamed awad.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rango/login.html', {})

'''
def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})

'''
def track_url(request):

    page_id = None
    url = '/rango/'

    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass
    return redirect(url)


def get_category_list(max_results=0, starts_with=''):
        cat_list = []
        if starts_with:
                cat_list = Category.objects.filter(name__istartswith=starts_with)

        if max_results > 0:
                if cat_list.count() > max_results:
                        cat_list = cat_list[:max_results]

        return cat_list


def suggest_category(request):

        cat_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['suggestion']

        cat_list = get_category_list(4, starts_with)

        return render(request, 'rango/cats.html', {'cat_list': cat_list })


@login_required
def user_logout(request):

    logout(request)
    return  HttpResponseRedirect('/rango/')


@login_required
def like_category(request):

    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()

    return HttpResponse(likes)



'''
@login_required
def update_profile(request):

    profile = None
    user = request.user
    try:
        profile = user.get_profile()
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user, ...)

    #you_profile = Userprofile.objects.get(user=request.user)
    form = UserprofileForm(initail={'bio':profile.bio})
    context = {'form': form }
    return  render(request, 'rango/update_profile.html',context)
'''


















 
