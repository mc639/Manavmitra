from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'post/(?P<slug>[\w-]+)/$', views.post, name="post"),
    url(r'category/(?P<slug>[\w-]+)/$', views.category, name="category"),
    url(r'epaper/$', views.epaper_main, name="epaper_main"),
    url(r'epaper/(?P<name>[\w\-]+)/$', views.epaper, name="epaper"),
    url(r'aboutus/$', views.aboutus, name="aboutus"),
]

handler400 = 'hindi.views.my_custom_bad_request_view'
handler403 = 'hindi.views.my_custom_permission_denied_view'
handler404 = 'hindi.views.my_custom_page_not_found_view'
handler500 = 'hindi.views.my_custom_error_view'
