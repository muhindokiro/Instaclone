from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^timeline/$',views.timeline,name = 'timeline'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^accounts/profile/$', views.timeline, name = 'timeline')
    
    # url(r'^login/$',views.login,name = 'login')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)