from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Import the vpn model
from django.contrib.auth.decorators import login_required
from ssn_demo.forms import UserForm, UserProfileForm, vpnForm

import ssn_demo
import vsd_functions
from vsd_functions import getDomains, addDomain

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


#def index(request):
#    return HttpResponse("Rango says: Hello world! <a href='/rango_app/about'>About</a>")

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render_to_response('ssn_demo/index.html', context_dict, context)


def about(request):
    return HttpResponse("Rango says: Here is the about page. <a href='/rango_app/'>Index</a>")

def listvpn(request):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the vpn passed by the user.
    vpn_dict = getDomains('')
    
    vpn_list = []
    
    for i in range(0, len(vpn_dict)): vpn_list.append(vpn_dict[i]['name'])
    
    context_dict = {'VPNS': vpn_list}

    return render_to_response('ssn_demo/vpns.html', context_dict, context)

def addvpn(request):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    if request.method == 'POST':

            vpn_name = request.POST.get('vpn_name', "")
            
    context_dict = addDomain(vpn_name)
    
    return render_to_response('ssn_demo/vpns.html', context_dict, context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'ssn_demo/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
    
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
                return HttpResponseRedirect('/ssn_demo/vpns/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your ssn_demo account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('ssn_demo/login.html', {}, context)
    

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/ssn_demo/')

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

