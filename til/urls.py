from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from feed import urls as feed_urls
from profiles import urls as profile_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(feed_urls, namespace="feed")),
    path('profile/', include(profile_urls, namespace="profiles")),
    re_path('', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
