from django.contrib import admin
from django.urls import include, path

from acme_project.settings import DEBUG

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
]

if DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
