from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
       (r'^$',TemplateView.as_view(template_name='home.html')),
       (r'^app$','socialshare.views.app_verification'),
       (r'^start$','socialshare.views.user_token'),
       (r'^verify$','socialshare.views.verify'),   
       (r'^start1$','socialshare.views.authenticate_user'),
       (r'^g/','socialshare.views.google_login'),
       (r'^g1/','socialshare.views.google_authenticate'),	
       )
	
	
