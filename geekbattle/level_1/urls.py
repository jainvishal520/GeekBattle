from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'level_1.views.ayf', name='home'),
	url(r'^profile', 'level_1.views.home',name='profile'),
	url(r'^start', 'level_1.views.start', name='start'),
	url(r'^question/(?P<qid>\d+)', 'level_1.views.question', name='question'),
	url(r'^submit', 'level_1.views.submit', name='submit'),
	url(r'^mark', 'level_1.views.mark', name='mark'),
	url(r'^question_list', 'level_1.views.question_list', name='question_list'),
	url(r'^question_json/(?P<qid>\d+)','level_1.views.question_json', name="question_json"),
	url(r'^answer_json','level_1.views.answer_json', name="answer_json"),
)

