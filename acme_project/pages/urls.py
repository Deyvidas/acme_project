from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path(route='', name='homepage',
         view=views.HomePage.as_view()),
]
