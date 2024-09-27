from django.contrib import admin
from django.urls import path, include  # Import include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    path('', include('myapp.urls')),  # Include the app URLs
]
