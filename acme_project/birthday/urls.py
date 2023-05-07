from django.urls import path

from . import views


app_name = 'birthday'

urlpatterns = [
    path('list/', views.get_list, name='list'),
    path('create/', views.crude_birthday, name='create'),
    path('<int:pk>/delete/', views.crude_birthday, name='delete'),
    path('<int:pk>/edit/', views.crude_birthday, name='edit'),
    path('<int:pk>/preview/', views.crude_birthday, name='preview'),
]
