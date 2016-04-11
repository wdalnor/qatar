from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from .models import Choice, Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse



def index(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    titles = "hello there ........ "
    if request.user.is_authenticated():
        
        titles="Welcome to Purchase Department Mr. of %s" %(request.user)
    home = "my home is so nice"
    context = {
        'latest_question_list': latest_question_list,
        'mytitle':titles,
        'homes':home,
    }
    
    
    
    return render(request, 'polls/index.html', context)
    '''
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
    return HttpResponse('<table>%s</table>' % ' \n'.join(html))
    '''    

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
        
    return render(request, 'polls/detail.html', {'question': question})
    
   

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):

    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detial.html', {
              'question':p,
              'error_message': " you did not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))




