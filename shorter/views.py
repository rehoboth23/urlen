from django.shortcuts import render, redirect
from .forms import Url_Form
from .models import Short_Url
from .shortner import Shortner


# Create your views here.
def make(request, token=None):
    print("in")
    form = Url_Form(request.POST)
    b = ""
    a = ""
    if request.method == 'GET':
        form = Url_Form
        return render(request, 'main.html', {'form': form, 'b': b})

    if request.method == 'POST':
        long_url = Short_Url.objects.filter(long_url=request.POST['long_url'])
        if long_url:
            b = long_url[0]
        else:
            if form.is_valid():
                new_url = form.save(commit=False)
                new_url.short_url = Shortner().issue_token()
                a = new_url
                new_url.save()
                form = form
            else:
                form = Url_Form()
                a = "Invalid Url"
    context = {
        'form': form,
        'a': a,
        'b':b
    }
    return render(request, 'main.html', context)


def to_url(request, token):
    long_url = Short_Url.objects.filter(short_url=token)[0]
    print(long_url.long_url)
    if long_url:
        return redirect(long_url.long_url)
    return redirect("shorten:make")