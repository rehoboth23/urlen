from django.urls import path
from shorter.views import to_url, make


app_name = 'shorten'
urlpatterns = [
    path('', make, name='make'),
    path('<str:token>', to_url, name='copy'),
]