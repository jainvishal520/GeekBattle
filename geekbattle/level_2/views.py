from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question
from .forms import DocumentForm
from level_1.models import Answer
# Create your views here.

def home(request):
	if request.method == "GET":
		return render(request,'level_1/home.html')	
	else:
		return render(request,'level_2/home.html')


def submit(request):
	if request.method == "GET":
		return render(request,'level_1/home.html')	
	else:
		obj=Answer.objects.get(user=request.user)
		choice = request.POST.get('re')
		form = DocumentForm()
		question = Question.objects.get(id=str(choice)) 
        	return render(request,
       		 'level_2/submit.html',
        	{'form': form,'question':question.description}
    		)

def save(request):
 if request.method == "GET":
		return render(request,'level_1/home.html')	
 else:
  form = DocumentForm(request.POST, request.FILES)
  obj=Answer.objects.get(user=request.user)
  if obj.s2 < 0:
   handle=open('/home/kushagra/PROJECTS/geekbattle/static/files/'+str(request.user),'w+b')
   if request.FILES == {}:	
    handle.write("Null")   
    handle.close()
   else:
    handle.write(request.FILES['docfile'].read())   
    handle.close()
   obj.s2=0	
   obj.save() 	
  return render(request,'level_1/home.html')					

