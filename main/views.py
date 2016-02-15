from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

from camera.models import Picture
from terrarium.helper import TerrariumHelper
from main.helper import MainHelper


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

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
                return HttpResponseRedirect('/main/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your karnipi account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('main/login.html', {}, context)


def user_logout(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

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

                return logout(request)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your karnipi account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.

    return logout(request)


@never_cache
def index(request):

    mh = MainHelper()

    latest_terrarium_data = TerrariumHelper().GetCurrentTerrariumData()
    today = datetime.today()
    latest_log_data = mh.get_karnipi_log().filter(datetime__year=today.year,
                                                  datetime__month=today.month,
                                                  datetime__day=today.day).order_by('-datetime')
												  
    picture = Picture.objects.latest('taken_on')
    status_overview = mh.get_status_overview()

    template = loader.get_template('main/index.html')
    context = RequestContext(request, {
        'latest_terrarium_data': latest_terrarium_data,
		'latest_picture': picture,
        'latest_log_data': latest_log_data,
        'status_overview': status_overview,
        'current_site': 'overview',
    })
    return HttpResponse(template.render(context))

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response