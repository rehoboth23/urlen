from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Url_Form
from .models import Short_Url
from .shortner import Shortner


# Create your views here.
def make(request):
    form = Url_Form(request.POST)
    b = ""
    a = ""
    if request.method == 'GET':
        form = Url_Form
        return render(request, 'index.html', {'form': form})
    if request.method == 'POST':
        new_url = Short_Url.objects.filter(long_url=request.POST['long_url'])
        if new_url:
            b = new_url[0]
        else:
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
        'a': a,
        'b':b
    }
    return render(request, 'index.html', context)


def home(request, token, copy=None):
    info = token.split(' ')
    if len(info)>1:
        id = int(info[2][1])
        long_url = Short_Url.objects.filter(id=id)[0]
        if copy:
            long_url.copy2clip(request.META.get('HTTP_REFERER'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(long_url.long_url)
    else:
        long_url = Short_Url.objects.filter(short_url=info[0])[0]
        return redirect(long_url.long_url)
