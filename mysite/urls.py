from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from dig import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^simple/$', views.file_upload, name='file_upload'),
    url(r'^uploaded/$', views.continue_to_data, name='continue_to_data'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
