from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from project.application.web_search....
from searchengine.web_search import *
from django.template import RequestContext

def search(request):

    if request.POST:
		return render_to_response(
			'search.html', 
			{'result': google(request.POST['term'], 10)}, 
			context_instance=RequestContext(request)
		)
    else:
		return render_to_response('search.html')