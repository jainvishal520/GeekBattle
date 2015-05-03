from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', RedirectView.as_view(url=reverse_lazy('level_1:home'))),
	url(r'^level_1/', include('level_1.urls',namespace='level_1')),	
	url(r'^level_2/', include('level_2.urls',namespace='level_2')),
	url(r'^level_3/', include('level_3.urls',namespace='level_3')),	
	url(r'^user/', include('UserAccount.urls',namespace='user')),
	url(r'^social/', include('socialshare.urls',namespace='user')),		
)
