from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', include("appUrls.urls")),
    path('db/', include("appDBcomponent.urls")),
    path('', include("appSamples.urls"))
]
