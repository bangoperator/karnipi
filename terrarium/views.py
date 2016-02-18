from __future__ import absolute_import

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.decorators.cache import never_cache

from .forms import ActorForm
from .models import TerrariumLog


@never_cache
def index(request):

    today = datetime.today()
    latest_terrarium_log = TerrariumLog.objects.all().filter(time__year=today.year,
                                                             time__month=today.month,
                                                             time__day=today.day).order_by('-time')

    template = loader.get_template('terrarium/index.html')
    context = RequestContext(request, {
        'latest_terrarium_log': latest_terrarium_log,
        'current_site': 'terrarium_data',
    })
    return HttpResponse(template.render(context))


def add_actor(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = ActorForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ActorForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('terrarium/add_actor.html', {'form': form}, context)
