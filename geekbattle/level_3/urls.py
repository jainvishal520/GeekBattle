from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'level_3.views.home', name='home'),
	url(r'^save/','level_3.views.save', name="save"),
)

