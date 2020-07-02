from django.shortcuts import render, redirect
from .forms import Url_Form
from .models import Short_Url
from .shortner import Shortner


# Create your views here.
def make(request):
    form = Url_Form(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            new_url = form.save(commit=False)
            a = Shortner().issue_token()
            new_url.short_url = a
            new_url.save()
        else:
            form = Url_Form()
            a = "Invalid Url"
    context = {
        'form': form,
        'a': a
    }
    return render(request, 'main.html', context)


def home(request, token):
    long_url = Short_Url.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)
