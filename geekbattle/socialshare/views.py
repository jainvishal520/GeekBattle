from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from twython import Twython
from level_1.models import Answer
import facebook
import urllib
import urllib2
import json

# google app details
google_client_id = '796645511249-tlfgn500o4tglgepp1m82tb41flstn9i.apps.googleusercontent.com'
google_client_secret= 'L-D3hYe5AWwo8SkqvQ8N85if'
google_redirect_uri = "http://geekbattle.asetalias.in/social/g1/"
# facebook app details
app_id ='633658320043143'
app_secret = '3d65ab8b848b79c213ab7bcd14862061'
post_login_url = 'http://geekbattle.asetalias.in/social/start'
# twitter app details
CONSUMER_KEY = 'CqXi0upPcOJt4mZnZnBmGZtXt'
CONSUMER_SECRET = 'I52uUKoMMPgTI6srdWwvDvIoCLOHhdf3OXideidY3fXauzKjux'
CALLBACK_URL='http://geekbattle.asetalias.in/social/verify'

passw= "asffsfasfjkalsnflaknlaskdl"
global session
session = dict()
answer_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
active_status_list = answer_list

#facebook verify app 
def app_verification(request):
 auth_url = ("http://www.facebook.com/dialog/oauth?" +
                               "client_id=" + app_id +
                               "&redirect_uri=" + post_login_url +
                              "&scope=email")
 return redirect(auth_url)

#facebook genrating access token 
def user_token(request):
 data = request.GET.get('code','')
 code_url = ("https://graph.facebook.com/oauth/access_token?" +
                               "client_id=" + app_id +
 			       "&client_secret=" + app_secret +  	
                               "&redirect_uri=" + post_login_url +
                               "&code=" + data)
 usock = urllib2.urlopen(code_url)
 data = usock.read()
 usock.close()
 acs_token = str(data).strip('access_token=')
 length = len(acs_token)-16
 acs_token = acs_token[0:length]
 graph = facebook.GraphAPI(acs_token)
 profile = graph.get_object("me")
 print profile['email']	
 if not(is_username_exist(profile['email'])):
    	user = User.objects.create_user(profile['email'],profile['email'],password = passw)
	Answer.objects.create(user=User.objects.get(username=profile['email']),answer_list=answer_list,active_status_list=active_status_list)
 user = auth.authenticate(username=profile['email'],password=passw)
 if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('level_1:home'))
 else:
            return HttpResponseRedirect(reverse('user:login'))



 

#twitter verify app 
def authenticate_user(request):
        twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET)
	auth = twitter.get_authentication_tokens(callback_url=CALLBACK_URL)
	session[0]= auth['oauth_token']
	session[1]= auth['oauth_token_secret']
	return redirect(auth['auth_url'])


def verify(request):
   oauth_verifier = request.GET['oauth_verifier']
   twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  session[0], session[1])
   final_step = twitter.get_authorized_tokens(oauth_verifier)
   OAUTH_TOKEN = final_step['oauth_token']
   OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
   twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
   twitter.verify_credentials()
   screen_name = twitter.verify_credentials()['screen_name']		
   if not(is_username_exist(screen_name)):
    	user = User.objects.create_user(username=screen_name,password = passw)
	Answer.objects.create(user=User.objects.get(username=screen_name),answer_list=answer_list,active_status_list=active_status_list)
   user = auth.authenticate(username=screen_name,password=passw)
   if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('level_1:home'))
   else:
            return HttpResponseRedirect(reverse('user:login'))
  

def google_login(request):
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = google_client_id
    redirect_uri = google_redirect_uri
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
        token_request_uri = token_request_uri,
        response_type = response_type,
        client_id = client_id,
        redirect_uri = redirect_uri,
        scope = scope)
    return HttpResponseRedirect(url)

def google_authenticate(request):
    login_failed_url = '/'
    if 'error' in request.GET or 'code' not in request.GET:
        return HttpResponseRedirect('{loginfailed}'.format(loginfailed = login_failed_url))

    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = google_redirect_uri
    params = urllib.urlencode({
        'code':request.GET['code'],
        'redirect_uri':redirect_uri,
        'client_id':google_client_id,
        'client_secret':google_client_secret,
        'grant_type':'authorization_code'
    })
    url_request = urllib2.Request(access_token_uri,params)
    response = urllib2.urlopen(url_request)
    data = response.read()
    token_data = json.loads(data)
    url = "https://www.googleapis.com/oauth2/v1/userinfo?access_token="+token_data['access_token']
    response = urllib2.urlopen(url).read()
    data = json.loads(response) 
    if not(is_username_exist(data['email'])):
    	user = User.objects.create_user(data['email'],data['email'],password = passw)
	Answer.objects.create(user=User.objects.get(username=data['email']),answer_list=answer_list,active_status_list=active_status_list)
    user = auth.authenticate(username=data['email'],password=passw)
    if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('level_1:home'))
    else:
            return HttpResponseRedirect(reverse('user:login'))
  


#Helper Function

def is_username_exist(username):
    if User.objects.filter(username=username).count():
        return True
    return False


