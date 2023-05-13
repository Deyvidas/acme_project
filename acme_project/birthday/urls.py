from django.urls import path

from . import views


app_name = 'birthday'

urlpatterns = [
    path(route='list/', name='list',
         view=views.BirthdayListView.as_view()),

    path(route='create/', name='create',
         view=views.BirthdayCreateView.as_view()),

    path(route='<int:pk>/delete/', name='delete',
         view=views.BirthdayDeleteView.as_view()),

    path(route='<int:pk>/edit/', name='edit',
         view=views.BirthdayUpdateView.as_view()),

    path(route='<int:pk>/preview/', name='preview',
         view=views.BirthdayDetailView.as_view()),
]
