from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'level_2.views.home', name='home'),
	url(r'^submit/', 'level_2.views.submit', name='submit'),
	url(r'^save/','level_2.views.save', name="save"),
	)


