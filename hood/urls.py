from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^new/profile$', views.addprofile, name='profile'),
    url(r'^new/viewprofile/(\d+)', views.viewprofile, name='viewprofile'),
    url(r'^new/edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^new/busine$', views.business, name='business'),
    # url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)