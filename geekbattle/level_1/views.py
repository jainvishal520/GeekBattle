import json
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Question
from .models import Answer, user_details
from .forms import register_form
from django.http import HttpResponse,HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import mechanize,cookielib

@login_required(login_url=reverse('user:login'))
def ayf(request):
	if request.method=='POST':
		form=register_form(request.POST)
		if form.is_valid():
			#details=user_details(detail_status=True,user=request.user,institute_filter=form.cleaned_data['institute_filter'],institute=form.cleaned_data['institute'],address=form.cleaned_data['address'],city=form.cleaned_data['city'],state=form.cleaned_data['state'],name=form.cleaned_data['name'],gender=form.cleaned_data['gender'],phone=form.cleaned_data['phone'],mobile=form.cleaned_data['mobile'],email=form.cleaned_data['email'])
			details=user_details(detail_status=True,user=request.user,institute_filter=form.cleaned_data['institute_filter'],institute=form.cleaned_data['institute'],address=form.cleaned_data['address'],city=form.cleaned_data['city'],state=form.cleaned_data['state'],name=form.cleaned_data['name'],gender=form.cleaned_data['gender'],phone=form.cleaned_data['phone'],mobile=form.cleaned_data['mobile'],email=form.cleaned_data['email'],prog=form.cleaned_data['prog'])
			details.save()
			if form.cleaned_data=='male':
				gender='M'
			else:
				gender='F'
			li=[[str(form.cleaned_data['institute_filter'])],[str(form.cleaned_data['state'])],[gender],['24'],['8'],['1994'],['0']]
			br = mechanize.Browser()
			cj = cookielib.LWPCookieJar()
			br.set_cookiejar(cj)
			br.set_handle_equiv(True)
			br.set_handle_gzip(True)
			br.set_handle_redirect(True)
			br.set_handle_referer(True)
			br.set_handle_robots(False)	
			br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
			br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
			br.open('http://www.amity.edu/ayf/webpages/website/Registerframe.aspx?eid=1037')
			br.select_form(name='form1')
			br.form.set_value(li[0], name='rdotype')
			br.form['txtinst']=form.cleaned_data['institute']
			br.form['txtaddress1']=form.cleaned_data['address']
			#br.form['txtaddress2'] = 'NA'
			br.form['txtcity'] = form.cleaned_data['city']
			br.form.set_value(li[1], name='ddlsatate')
			br.form['txtname'] = form.cleaned_data['name']
			br.form['txtprog'] = form.cleaned_data['prog']
			br.form.set_value(li[2], name='rdogender')
			br.form.set_value(li[3], name='ddl2_date')
			br.form.set_value(li[4], name='ddl3_month')
			br.form.set_value(li[5], name='ddl4_year')
			br.form['txtdob'] = '24/08/1994'
			br.form['txtmobile'] = form.cleaned_data['mobile']
			br.form['email'] = form.cleaned_data['email']
			br.form.set_value(['0'], name='rdoacomd')
			br.submit()
			return HttpResponseRedirect(reverse('level_1:profile'))
		else:
			form=register_form(request.POST)
			context={'form':form}
			return render_to_response('level_1/register.html',context,context_instance=RequestContext(request))
	else:
		# try:
		# 	details=user_details.objects.get(user=request.user)
		# except user_details.DoesNotExist:
		# 	form=register_form(request.POST)
		# 	context={'form':form}
		# 	return render_to_response('level_1/register.html',context,context_instance=RequestContext(request))
		# else:
		# 	return HttpResponseRedirect(reverse('level_1:profile'))

		if user_details.objects.filter(user__username=request.user.username).exists():
			return HttpResponseRedirect(reverse('level_1:profile'))
		else:
			form=register_form(request.POST)
			context={'form':form}
			return render_to_response('level_1/register.html',context,context_instance=RequestContext(request))
	

@login_required(login_url=reverse('user:login'))
def home(request):
	 return render(request,'level_1/home.html')	


@login_required(login_url=reverse('user:login'))
def start(request):
	if request.method == "GET":
		return render(request,'level_1/home.html')
	elif request.method == "POST":
		obj = Answer.objects.get(user=request.user)
		if obj.s1 >= 0:
		 return render(request,'level_1/home.html')		
		choice = request.POST.get('re')
		qid = request.POST.get('qid1')
		if qid is None:
			return render(request,'level_1/display.html',{'qid' : 1})
		answer_list = json.loads(obj.answer_list)
		if str(choice) == str(answer_list[int(qid)-1]):
			choice = "0"
		answer_list[int(qid)-1]=int(choice)
		obj.answer_list=answer_list
		obj.save()
		return render(request,'level_1/display.html',{'qid' : qid})

@login_required(login_url=reverse('user:login'))
def question(request,qid):
	return render(request,'level_1/question.html',{'qid' : qid})

@login_required(login_url=reverse('user:login'))
def submit(request):
	obj = Answer.objects.get(user=request.user)	
	answer_list = json.loads(obj.answer_list)
	obj.s1=0
	temp=1
	question_list = Question.objects.all()
	for i in question_list:
		question_obj = Question.objects.get(id=str(temp))
		if answer_list[temp] == question_obj.answer:
			obj.s1 = int(obj.s1) +1
		temp += 1
	obj.s1 = (float(obj.s1)/(temp-1))*100
	obj.save()
	return HttpResponseRedirect(reverse('level_1:home'))

@login_required(login_url=reverse('user:login'))
def mark(request):
	qid = request.POST.get('qid2')
	obj=Question.objects.get(id=str(qid))
	answer_obj = Answer.objects.get(user=request.user)	
	data = json.loads(answer_obj.active_status_list)
	data[int(qid)-1]=int(request.POST.get('name'))
	answer_obj.active_status_list=data
	answer_obj.save()
	obj.save()
	return render(request,'level_1/display.html',{'qid' : qid})

@login_required(login_url=reverse('user:login'))
def question_list(request):
	question_list = Question.objects.all()
	question_list_array = []
  	for i in question_list:
  		question_list_dic = question_list_dictionary(request,i)
   		question_list_array.append(question_list_dic)
  	return HttpResponse(json.dumps(question_list_array,cls=DjangoJSONEncoder), content_type="application/json")


def question_list_dictionary(request,question):
	temp = {}
	obj = Answer.objects.get(user=request.user)	
	data = json.loads(obj.answer_list)
	temp["id"] = question.id
	temp["answer"] = data[question.id-1]
	data = json.loads(obj.active_status_list)
   	temp["active_status"] = data[question.id-1]
   	temp["choice_1"] = question.choice_1
	temp["choice_2"] = question.choice_2
	temp["choice_3"] = question.choice_3
	temp["choice_4"] = question.choice_4
   	temp["description"] = question.description
	temp["count"]=0	
	data = json.loads(obj.answer_list)
	index=0
	for i in data:
		if data[index] != 0:
			temp["count"] += 1
		index += 1
	return temp

@login_required(login_url=reverse('user:login'))
def question_json(request,qid):
	question_array = []
	question_obj = Question.objects.get(id=qid)
	data=question_list_dictionary(request,question_obj)
	question_array.append(data)
	return HttpResponse(json.dumps(question_array,cls=DjangoJSONEncoder), content_type="application/json")

def answer_json(request):
	answer_array = []	
	answer_obj = Answer.objects.get(user=request.user)
	data=answer_dictionary(request,answer_obj)
	answer_array.append(data)
	return HttpResponse(json.dumps(answer_array,cls=DjangoJSONEncoder), content_type="application/json")

def answer_dictionary(request,answer1):
	temp = {}
	temp["user"] = answer1.user.username
	temp["answer_list"] = json.loads(answer1.answer_list)
	temp["active_status_list"] = json.loads(answer1.active_status_list)
	temp["s1"] = answer1.s1
	temp["s2"] = answer1.s2
	temp["s3"] = answer1.s3
	return temp        

