from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm


# Create your views here.

def frontpage(request):
    return render(request, 'frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # check if passwords are matching
        if form.is_valid():
            user = form.save()

            login(request, user)

            # 'frontpage' points to the urls.py and finds a view with this name
            return redirect('frontpage')

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
