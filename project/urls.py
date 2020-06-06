from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('', views.homepage, name ='homepage'),
    path('search/', views.search_results, name='search_project'),
    path('profile/',views.profile, name = "profile"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
