from django.urls import path
from .views import home
from .views import download_cv

urlpatterns = [
    path('home/', home, name='home'),
    path('download-cv/', download_cv, name='download_cv'),
]
